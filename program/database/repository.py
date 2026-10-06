"""公开数据到 Phase 1 的适配，以及私有评估的独立存储入口。"""

import json
from datetime import date

from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from .models import HazardRules, SolventData, UserEvaluations, utc_now
from .validation import text_value


def export_hsp_database(
    session: Session, *, include_demo: bool = False, as_of: date | None = None
) -> dict:
    """返回 records 与 skipped；缺少 HSP/评分的溶剂不填零且明确列出。"""
    day = as_of or utc_now().date()
    solvents_query = select(SolventData).order_by(SolventData.cas)
    if not include_demo:
        solvents_query = solvents_query.where(SolventData.is_demo.is_(False))
    rules = session.scalars(
        select(HazardRules).where(
            HazardRules.active.is_(True),
            HazardRules.exclude_from_recommendations.is_(True),
            or_(HazardRules.effective_from.is_(None), HazardRules.effective_from <= day),
            or_(HazardRules.effective_to.is_(None), HazardRules.effective_to >= day),
        )
    ).all()
    excluded = {(rule.cas, rule.is_demo) for rule in rules}
    records, skipped = [], []
    for solvent in session.scalars(solvents_query):
        missing = [
            field
            for field in ("delta_d", "delta_p", "delta_h", "gsk_score", "score_source")
            if getattr(solvent, field) is None
        ]
        if missing:
            skipped.append({"cas": solvent.cas, "name": solvent.name, "missing_fields": missing})
            continue
        source = solvent.field_sources.get("delta_d")
        source_label = (
            None
            if not source
            else (f"{source['source_id']}@{source['version']}: {source['location']}")
        )
        records.append(
            {
                "cas": solvent.cas,
                "name": solvent.name,
                "delta_d": solvent.delta_d,
                "delta_p": solvent.delta_p,
                "delta_h": solvent.delta_h,
                "gsk_score": solvent.gsk_score,
                "boiling_point": solvent.boiling_point,
                "flash_point": solvent.flash_point,
                "hsp_temperature_c": solvent.hsp_temperature_c,
                "score_source": solvent.score_source,
                "source": source_label,
                "excluded": solvent.excluded or (solvent.cas, solvent.is_demo) in excluded,
                "is_demo": solvent.is_demo,
            }
        )
    return {"records": records, "skipped": skipped, "as_of": day.isoformat()}


def save_evaluation(
    session: Session,
    *,
    reaction: str,
    amounts: dict,
    evaluation_result: dict,
    waste_boundary: str,
    scoring_version: str,
    mass_unit: str = "g",
    user_id: str | None = None,
    input_format: str = "json",
    dataset_versions: dict | None = None,
) -> UserEvaluations:
    """保存私有快照，事务由调用方控制。此接口不重新计算或认证用户结果。"""
    if mass_unit not in ("g", "kg", "mg"):
        raise ValueError("mass_unit 必须为 g/kg/mg")
    if input_format not in ("json", "csv", "smiles", "manual"):
        raise ValueError("input_format 必须为 json/csv/smiles/manual")
    if user_id is not None:
        user_id = text_value(user_id, "user_id", 100)
    snapshot = {
        "amounts": amounts,
        "evaluation_result": evaluation_result,
        "dataset_versions": {} if dataset_versions is None else dataset_versions,
    }
    if any(not isinstance(value, dict) for value in snapshot.values()):
        raise ValueError("用量、结果和数据版本必须为 JSON 对象")
    # 深拷贝避免调用方事后修改传入字典，严格拒绝 NaN、Infinity。
    snapshot = json.loads(json.dumps(snapshot, ensure_ascii=False, allow_nan=False))
    evaluation = UserEvaluations(
        reaction=text_value(reaction, "reaction"),
        user_id=user_id,
        waste_boundary=text_value(waste_boundary, "waste_boundary"),
        scoring_version=text_value(scoring_version, "scoring_version", 100),
        mass_unit=mass_unit,
        input_format=input_format,
        **snapshot,
    )
    session.add(evaluation)
    session.flush()
    return evaluation
