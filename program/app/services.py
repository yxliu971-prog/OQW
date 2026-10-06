"""将 Phase 1 指标和 Phase 2 数据层组合，不在路由中重复化学规则。"""

from decimal import Decimal
from math import fsum

from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from chem_engine import (
    build_radar_data,
    calculate_atom_economy_stoichiometric,
    calculate_e_factor,
    calculate_green_score,
    calculate_rme,
    find_green_replacements,
)
from database.models import HazardRules, SolventData, utc_now
from database.repository import export_hsp_database, save_evaluation

from .errors import APIError
from .schemas import EvaluationRequest, SolventReference, SwapRequest


def resolve_solvent(
    session: Session, reference: SolventReference, allow_demo: bool
) -> SolventData | None:
    query = select(SolventData)
    if not allow_demo:
        query = query.where(SolventData.is_demo.is_(False))
    if reference.cas:
        item = session.scalar(query.where(SolventData.cas == reference.cas))
        if item and reference.name and item.name.casefold() != reference.name.casefold():
            raise APIError(
                422, "solvent_identifier_mismatch", "CAS 与名称不对应，请核对或只提供 CAS"
            )
        if item is None:
            rules = select(HazardRules).where(HazardRules.cas == reference.cas)
            if not allow_demo:
                rules = rules.where(HazardRules.is_demo.is_(False))
            rule = session.scalar(rules.order_by(HazardRules.source_id))
            if rule:
                # 地方规则可以独立识别 CAS，不要求它已在溶剂物性表中存在。
                item = SolventData(
                    cas=rule.cas,
                    name=rule.name,
                    is_demo=rule.is_demo,
                    excluded=False,
                    field_sources={"name": rule.provenance},
                )
        return item
    # 名称精确匹配，Unicode casefold 在 Python 中处理；不猜测模糊同义词。
    matches = [
        item for item in session.scalars(query) if item.name.casefold() == reference.name.casefold()
    ]
    if len(matches) > 1:
        raise APIError(409, "ambiguous_solvent_name", "名称对应多个溶剂，请提供 CAS")
    if matches:
        return matches[0]
    rules = select(HazardRules)
    if not allow_demo:
        rules = rules.where(HazardRules.is_demo.is_(False))
    matches_by_cas = {
        rule.cas: rule
        for rule in session.scalars(rules)
        if rule.name.casefold() == reference.name.casefold()
    }
    if len(matches_by_cas) > 1:
        raise APIError(409, "ambiguous_solvent_name", "名称对应多个物质，请提供 CAS")
    if matches_by_cas:
        return resolve_solvent(
            session, SolventReference(cas=next(iter(matches_by_cas))), allow_demo
        )
    return None


def active_rules(session: Session, solvent: SolventData) -> list[HazardRules]:
    today = utc_now().date()
    return list(
        session.scalars(
            select(HazardRules)
            .where(
                HazardRules.cas == solvent.cas,
                HazardRules.is_demo == solvent.is_demo,
                HazardRules.active.is_(True),
                or_(HazardRules.effective_from.is_(None), HazardRules.effective_from <= today),
                or_(HazardRules.effective_to.is_(None), HazardRules.effective_to >= today),
            )
            .order_by(HazardRules.source_id, HazardRules.rule_code)
        )
    )


def solvent_summary(solvent: SolventData) -> dict:
    return {
        "cas": solvent.cas,
        "name": solvent.name,
        "gsk_score": solvent.gsk_score,
        "score_source": solvent.score_source,
        "boiling_point": solvent.boiling_point,
        "flash_point": solvent.flash_point,
        "ghs_codes": solvent.ghs_codes,
        "excluded": solvent.excluded,
        "is_demo": solvent.is_demo,
        "field_sources": solvent.field_sources,
        "raw_scores": solvent.raw_scores,
    }


def evaluate_reaction(session: Session, request: EvaluationRequest, *, allow_demo: bool) -> dict:
    """只计算、不提交；调用方可选择保存，也可批量诊断后统一提交成功行。"""
    try:
        ae = calculate_atom_economy_stoichiometric(
            [item.smiles for item in request.reactants],
            request.product.smiles,
            reactant_coefficients=[item.coefficient for item in request.reactants],
            product_coefficient=request.product.coefficient,
        )
        total_reactants_mass = fsum(item.mass for item in request.reactants)
        rme = calculate_rme(request.product.mass, total_reactants_mass)
        ef = (
            None
            if request.total_waste_mass is None
            else calculate_e_factor(request.total_waste_mass, request.product.mass)
        )
    except (ValueError, OverflowError) as exc:
        raise APIError(422, "invalid_chemistry_input", str(exc)) from exc

    warnings, solvents, notes = [], [], []
    versions = {"solvents": {}, "hazards": {}}
    resolved = []
    seen = set()
    for reference in request.solvents:
        solvent = resolve_solvent(session, reference, allow_demo)
        if solvent is None:
            solvents.append(
                {
                    "cas": reference.cas,
                    "name": reference.name,
                    "mass": reference.mass,
                    "status": "unknown",
                    "gsk_score": None,
                }
            )
            warnings.append(
                {
                    "cas": reference.cas,
                    "name": reference.name,
                    "severity": "warning",
                    "code": "unknown_solvent",
                    "message": "数据库中没有该溶剂，危害和绿色等级未评估",
                }
            )
            resolved.append((reference, None))
            continue
        if solvent.cas in seen:
            raise APIError(422, "duplicate_solvent", "同一溶剂请合并用量后提交，不能重复列入")
        seen.add(solvent.cas)
        resolved.append((reference, solvent))
        solvents.append({**solvent_summary(solvent), "mass": reference.mass, "status": "known"})
        versions["solvents"][solvent.cas] = solvent.field_sources
        if isinstance(solvent.raw_scores, dict):
            if solvent.raw_scores.get("mapping"):
                notes.append(f"{solvent.cas} 评分依据：{solvent.raw_scores['mapping']}")
            if solvent.raw_scores.get("caveat"):
                notes.append(f"{solvent.cas} 来源附注：{solvent.raw_scores['caveat']}")
        if solvent.gsk_score is not None and solvent.gsk_score <= 6:
            warnings.append(
                {
                    "cas": solvent.cas,
                    "name": solvent.name,
                    "severity": "danger" if solvent.gsk_score <= 3 else "warning",
                    "code": "low_green_score",
                    "message": "溶剂绿色等级较低，可查看替换候选",
                    "score": solvent.gsk_score,
                    "basis": "OQW 提示阈值：≤3 红色，(3,6] 黄色；非毒理结论",
                }
            )
        if solvent.ghs_codes:
            warnings.append(
                {
                    "cas": solvent.cas,
                    "name": solvent.name,
                    "severity": "warning",
                    "code": "ghs_hazards",
                    "message": "数据库记录了 GHS 危险代码，请结合 SDS 与工艺条件核验",
                    "ghs_codes": solvent.ghs_codes,
                }
            )
        elif solvent.ghs_codes is None:
            notes.append(f"{solvent.cas} 缺少 GHS 数据，不能据此认定无危害。")
        if solvent.excluded:
            warnings.append(
                {
                    "cas": solvent.cas,
                    "name": solvent.name,
                    "severity": "danger",
                    "code": "excluded_solvent",
                    "message": "该溶剂被上游候选策略明确排除",
                }
            )
        for rule in active_rules(session, solvent):
            warnings.append(
                {
                    "cas": solvent.cas,
                    "name": solvent.name,
                    "severity": rule.severity,
                    "code": "hazard_rule",
                    "rule_code": rule.rule_code,
                    "rule_type": rule.rule_type,
                    "message": rule.warning,
                    "conditions": rule.conditions,
                    "is_svhc": rule.is_svhc,
                    "exclude_from_recommendations": rule.exclude_from_recommendations,
                    "source": rule.provenance,
                }
            )
            versions["hazards"][f"{rule.source_id}:{rule.rule_code}:{rule.cas}"] = rule.provenance

    solvent_grade = None
    known = [solvent for _, solvent in resolved if solvent is not None]
    complete = (
        len(known) == len(resolved)
        and bool(known)
        and all(solvent.gsk_score is not None and solvent.score_source for solvent in known)
    )
    if (
        complete
        and len({solvent.score_source for solvent in known}) == 1
        and len({solvent.is_demo for solvent in known}) == 1
    ):
        if len(resolved) == 1:
            solvent_grade = known[0].gsk_score
        elif all(reference.mass is not None for reference, _ in resolved):
            total_solvent_mass = fsum(reference.mass for reference, _ in resolved)
            solvent_grade = fsum(
                reference.mass / total_solvent_mass * solvent.gsk_score
                for reference, solvent in resolved
            )
            notes.append(
                "混合溶剂等级为同评分口径下的质量加权平均，仅用于 OQW 指标，不代表混合物危害评级。"
            )
    if solvent_grade is None:
        notes.append("溶剂维度未评估：未提供溶剂，或缺少身份/等级/可比评分来源/混合用量。")
    if ef is None:
        notes.append("未提供总废弃物质量，E-Factor 与废弃物维度保持未评估，不以反应物减产物代替。")
    demo = any(solvent.is_demo for solvent in known)
    if demo:
        notes.append("本次使用合成演示数据，不可用于实际化学或法规判断。")
    score = calculate_green_score(
        ae,
        ef,
        rme,
        solvent_green_score=solvent_grade,
        energy_efficiency_score=request.energy_assessment.score
        if request.energy_assessment
        else None,
        process_safety_score=request.process_safety_assessment.score
        if request.process_safety_assessment
        else None,
    )
    score["external_assessments"] = {
        "energy": request.energy_assessment.model_dump() if request.energy_assessment else None,
        "process_safety": request.process_safety_assessment.model_dump()
        if request.process_safety_assessment
        else None,
        "source": "由调用方提供；OQW 不将其标为权威认证分数",
    }
    return {
        "evaluation_id": None,
        "evaluated_at": utc_now().isoformat(),
        "metrics": {"atom_economy": ae, "e_factor": ef, "rme": rme},
        "score": score,
        "radar": build_radar_data(score),
        "solvent_warnings": warnings,
        "solvents": solvents,
        "data_notes": notes,
        "dataset_versions": versions,
        "mass_basis": {
            "unit": request.mass_unit,
            "total_reactants_mass": total_reactants_mass,
            "product_mass": request.product.mass,
            "total_waste_mass": request.total_waste_mass,
            "waste_boundary": request.waste_boundary,
        },
        "demo_only": demo,
    }


def persist_evaluation(
    session: Session, request: EvaluationRequest, result: dict, *, input_format: str = "json"
) -> None:
    reaction = ".".join(item.smiles for item in request.reactants) + ">>" + request.product.smiles
    record = save_evaluation(
        session,
        reaction=reaction,
        amounts=request.model_dump(exclude={"persist"}),
        evaluation_result=result,
        waste_boundary=request.waste_boundary or "未声明；E-Factor 未评估",
        scoring_version=result["score"]["scoring_version"],
        mass_unit=request.mass_unit,
        input_format=input_format,
        dataset_versions=result["dataset_versions"],
    )
    result["evaluation_id"] = record.id
    # 保存的快照也带同一个 ID；JSON 修改采用整体赋值。
    record.evaluation_result = {**result}


def cost_estimate(request: SwapRequest, target_cas: str, candidate_cas: str) -> dict:
    context = request.cost_context
    if context is None:
        return {
            "status": "unavailable",
            "reason": "未提供同地区、同日期、同币种的处置报价",
            "original_cost": None,
            "replacement_cost": None,
            "difference": None,
        }
    quotes = {quote.cas: quote for quote in context.quotes}
    if target_cas not in quotes or candidate_cas not in quotes:
        return {
            "status": "unavailable",
            "reason": "原溶剂或候选缺少报价",
            "original_cost": None,
            "replacement_cost": None,
            "difference": None,
        }
    mass = Decimal(str(context.waste_mass_kg))
    original = mass * Decimal(str(quotes[target_cas].cost_per_kg))
    replacement = mass * Decimal(str(quotes[candidate_cas].cost_per_kg))
    return {
        "status": "estimated",
        "original_cost": float(round(original, 2)),
        "replacement_cost": float(round(replacement, 2)),
        "difference": float(round(replacement - original, 2)),
        "currency": context.currency,
        "region": context.region,
        "quote_date": context.quote_date,
        "waste_mass_kg": context.waste_mass_kg,
        "original_quote": quotes[target_cas].model_dump(),
        "replacement_quote": quotes[candidate_cas].model_dump(),
        "assumption": (
            "假设废弃物质量与处置类别可比，仅计给定单价；差额=候选−原溶剂，不含工艺改造成本"
        ),
    }


def recommend_swap(session: Session, request: SwapRequest, *, allow_demo: bool) -> dict:
    target = resolve_solvent(session, request, allow_demo)
    if target is None:
        raise APIError(
            404, "solvent_not_found", "数据库中没有目标溶剂，请先导入数据或核对 CAS/名称"
        )
    exported = export_hsp_database(session, include_demo=allow_demo)
    records = [row for row in exported["records"] if row["is_demo"] == target.is_demo]
    if not any(row["cas"] == target.cas for row in records):
        details = next((row for row in exported["skipped"] if row["cas"] == target.cas), None)
        raise APIError(
            422, "incomplete_solvent_data", "目标缺少 HSP 或可追溯的绿色评分，无法排序", details
        )
    replacements = find_green_replacements(target.cas, records, request.top_k)
    for candidate in replacements:
        candidate["disposal_cost"] = cost_estimate(request, target.cas, candidate["cas"])
    return {
        "status": "ok" if replacements else "no_candidates",
        "target": solvent_summary(target),
        "replacements": replacements,
        "skipped": exported["skipped"],
        "notes": [
            "先筛选更高绿色等级和未禁选候选，再按 HSP 距离排序；不保证反应兼容性。",
            "已知温度或评分口径不同的记录不混排，演示与生产溶剂不混排。",
        ],
        "demo_only": target.is_demo,
    }
