"""OQW 绿色化学指标与透明评分规则。

AE 使用 RDKit 平均摩尔质量（g/mol），不使用单同位素精确质量。
E-Factor、RME 的质量单位由调用者统一，例如均为 g 或均为 kg。
评分是 OQW 工程规则，不是 GSK、ACS 或任何机构认证结论。
"""

from collections import Counter
from collections.abc import Mapping, Sequence
from math import fsum, isfinite

from rdkit import Chem
from rdkit.Chem import Descriptors

from ._validation import number

SCORING_VERSION = "oqw-v1.0"
DEFAULT_WEIGHTS = {
    "atom_economy": 0.20,
    "reaction_mass_efficiency": 0.20,
    "waste_prevention": 0.20,
    "solvent_greenness": 0.20,
    "energy_efficiency": 0.10,
    "process_safety": 0.10,
}
DIMENSION_LABELS = {
    "atom_economy": "原子经济性",
    "reaction_mass_efficiency": "反应质量效率",
    "waste_prevention": "废弃物减量",
    "solvent_greenness": "溶剂绿色度",
    "energy_efficiency": "能源效率",
    "process_safety": "工艺安全",
}


def _parse_smiles(smiles: str, label: str) -> Chem.Mol:
    if not isinstance(smiles, str) or not smiles.strip():
        raise ValueError(f"{label} 必须是非空 SMILES 字符串")
    smiles = smiles.strip()
    # 禁止 RDKit 将空格后的垃圾输入当作分子名称而悄悄接受。
    if any(character.isspace() for character in smiles):
        raise ValueError(f"{label} 只接受 SMILES，不接受名称或 CXSMILES 注释")
    params = Chem.SmilesParserParams()
    params.parseName = False
    params.allowCXSMILES = False
    molecule = Chem.MolFromSmiles(smiles, params)
    if molecule is None or molecule.GetNumAtoms() == 0:
        raise ValueError(f"{label} 不是有效的 SMILES: {smiles!r}")
    if any(atom.GetAtomicNum() == 0 or atom.HasQuery() for atom in molecule.GetAtoms()):
        raise ValueError(f"{label} 不能包含通配原子或查询结构")
    return molecule


def molecular_weight(smiles: str) -> float:
    """返回平均摩尔质量，单位 g/mol；无效 SMILES 抛出 ValueError。"""
    return number(Descriptors.MolWt(_parse_smiles(smiles, "smiles")), "摩尔质量", positive=True)


def _atom_inventory(molecule: Chem.Mol) -> Counter:
    # 显式补氢后检查目标产物没有凭空多出的元素/同位素，包括氢。
    # 此检查仅是必要条件，不能代替完整反应配平或化学可行性验证。
    return Counter(
        (atom.GetAtomicNum(), atom.GetIsotope()) for atom in Chem.AddHs(molecule).GetAtoms()
    )


def calculate_atom_economy(reactants_smiles: list[str], target_product_smiles: str) -> float:
    """计算 AE (%)：MW(目标产物) / Σ MW(计量反应物) × 100。

    此简明接口默认每个列表项和目标产物的化学计量系数均为 1。
    整数系数可重复传入 SMILES；一般系数使用下方 stoichiometric 接口。
    不应包含纯溶剂/催化剂；消耗的计量试剂必须纳入。允许省略副产物。
    """
    return calculate_atom_economy_stoichiometric(reactants_smiles, target_product_smiles)


def calculate_atom_economy_stoichiometric(
    reactants_smiles: list[str],
    target_product_smiles: str,
    *,
    reactant_coefficients: Sequence[float] | None = None,
    product_coefficient: float = 1.0,
) -> float:
    """AE = νp × MWp / Σ(νi × MWi) × 100；系数是配平系数而非实际投料比。"""
    if not isinstance(reactants_smiles, list) or not reactants_smiles:
        raise ValueError("reactants_smiles 必须为非空 SMILES 列表")
    if reactant_coefficients is None:
        coefficients = [1.0] * len(reactants_smiles)
    else:
        if isinstance(reactant_coefficients, (str, bytes)) or not isinstance(
            reactant_coefficients, Sequence
        ):
            raise ValueError("reactant_coefficients 必须为数值序列")
        if len(reactant_coefficients) != len(reactants_smiles):
            raise ValueError("化学计量系数数量必须与反应物数量一致")
        coefficients = [
            number(value, f"reactant_coefficients[{index}]", positive=True)
            for index, value in enumerate(reactant_coefficients)
        ]
    product_coefficient = number(product_coefficient, "product_coefficient", positive=True)
    reactants = [
        _parse_smiles(value, f"reactants_smiles[{index}]")
        for index, value in enumerate(reactants_smiles)
    ]
    product = _parse_smiles(target_product_smiles, "target_product_smiles")

    # 同时缩放系数，既不改变 AE，又避免极大系数乘分子量导致溢出。
    scale = max(*coefficients, product_coefficient)
    coefficients = [value / scale for value in coefficients]
    product_coefficient /= scale
    if product_coefficient == 0 or any(value == 0 for value in coefficients):
        raise ValueError("化学计量系数比例超出可计算的浮点精度范围")
    available: Counter = Counter()
    for molecule, coefficient in zip(reactants, coefficients, strict=True):
        for element, count in _atom_inventory(molecule).items():
            available[element] += count * coefficient
    for element, count in _atom_inventory(product).items():
        required = count * product_coefficient
        if required > available[element] + 1e-9 * max(required, available[element]):
            raise ValueError("目标产物的元素/同位素用量超过反应物；请检查结构和配平系数")

    denominator = fsum(
        Descriptors.MolWt(molecule) * coefficient
        for molecule, coefficient in zip(reactants, coefficients, strict=True)
    )
    result = Descriptors.MolWt(product) * product_coefficient / denominator * 100
    if not isfinite(result) or result > 100 + 1e-8:
        raise ValueError("AE 超出 0–100%，请检查反应物是否完整、系数是否正确")
    return min(100.0, result)  # 仅消除浮点舍入误差，不掩盖实质性输入错误。


def calculate_e_factor(total_waste_mass: float, product_mass: float) -> float:
    """E-Factor = 废弃物质量 / 分离目标产物质量（同单位）。

    废弃物应按声明的系统边界汇总：副产物、废溶剂、处理废物等。
    是否含水、如何处理回收物流由调用者明确；本函数不推算或扣减。
    目标产物质量为零时无法定义 E-Factor，抛出 ValueError。
    """
    waste = number(total_waste_mass, "total_waste_mass", minimum=0)
    product = number(product_mass, "product_mass", positive=True)
    return number(waste / product, "E-Factor", minimum=0)


def calculate_rme(product_mass: float, total_reactants_mass: float) -> float:
    """RME (%) = 分离目标产物质量 / 实际投入反应物总质量 × 100。

    反应物包括过量试剂，不包含纯溶剂和未消耗催化剂；不是总工艺投料。
    大于 100% 说明质量口径/输入异常，直接报错而非截断。
    """
    product = number(product_mass, "product_mass", minimum=0)
    reactants = number(total_reactants_mass, "total_reactants_mass", positive=True)
    if product > reactants:
        raise ValueError("product_mass 不能大于 total_reactants_mass；请检查单位和投料完整性")
    return product / reactants * 100


def calculate_green_score(
    atom_economy: float,
    e_factor: float | None,
    rme: float,
    *,
    solvent_green_score: float | None = None,
    energy_efficiency_score: float | None = None,
    process_safety_score: float | None = None,
    weights: Mapping[str, float] | None = None,
    e_factor_half_score: float = 10.0,
) -> dict:
    """返回 0–100 综合分、六维得分、覆盖率和评分方法版本。

    AE/RME 直接使用百分数；废弃物分 = 100 / (1 + E/E50)。
    E-Factor 未评估时传 None，废弃物维度保持缺失，不推测废物质量。
    溶剂分 = (绿色等级 - 1) / 9 × 100，等级 1–10 且越高越好。
    能源/安全分需调用方提供经独立规则评估的 0–100 分，缺失为 None。
    缺失维度不计入加权平均；因此部分评分不可当作完整绿色度结论。
    所有权重均须提供（可设 0 禁用），函数自动归一化。
    """
    ae = number(atom_economy, "atom_economy", minimum=0, maximum=100)
    ef = None if e_factor is None else number(e_factor, "e_factor", minimum=0)
    rme_value = number(rme, "rme", minimum=0, maximum=100)
    half = number(e_factor_half_score, "e_factor_half_score", positive=True)
    # 分支等价变换避免极端有限数值相除产生 inf。
    waste_score = None
    if ef is not None:
        waste_score = 100 / (1 + ef / half) if ef <= half else 100 * (half / ef) / (1 + half / ef)
    dimensions = {
        "atom_economy": ae,
        "reaction_mass_efficiency": rme_value,
        "waste_prevention": waste_score,
        "solvent_greenness": (
            None
            if solvent_green_score is None
            else (number(solvent_green_score, "solvent_green_score", minimum=1, maximum=10) - 1)
            / 9
            * 100
        ),
        "energy_efficiency": (
            None
            if energy_efficiency_score is None
            else number(energy_efficiency_score, "energy_efficiency_score", minimum=0, maximum=100)
        ),
        "process_safety": (
            None
            if process_safety_score is None
            else number(process_safety_score, "process_safety_score", minimum=0, maximum=100)
        ),
    }
    supplied = dict(DEFAULT_WEIGHTS) if weights is None else weights
    if not isinstance(supplied, Mapping) or set(supplied) != set(dimensions):
        raise ValueError("weights 必须包含全部六个维度且不能含未知维度")
    validated = {key: number(value, f"weights.{key}", minimum=0) for key, value in supplied.items()}
    scale = max(validated.values())
    if scale == 0:
        raise ValueError("至少一个权重必须大于 0")
    total = fsum(value / scale for value in validated.values())
    normalized = {key: (value / scale) / total for key, value in validated.items()}
    observed = {
        key: value for key, value in dimensions.items() if value is not None and normalized[key] > 0
    }
    coverage = fsum(normalized[key] for key in observed)
    if coverage == 0:
        raise ValueError("至少一个已评估维度必须具有正权重")
    missing = [key for key, value in dimensions.items() if value is None]
    missing_weighted = [key for key in missing if normalized[key] > 0]
    overall = fsum(value * (normalized[key] / coverage) for key, value in observed.items())
    return {
        "overall_score": round(min(100.0, overall), 4),
        "dimension_scores": {
            key: None if value is None else round(value, 4) for key, value in dimensions.items()
        },
        "weights": normalized,
        "effective_weights": {key: normalized[key] / coverage for key in observed},
        "coverage": round(coverage, 6),
        "status": "partial" if missing_weighted else "complete",
        "missing_dimensions": missing,
        "scoring_version": SCORING_VERSION,
        "method": {"e_factor_half_score": half, "source": "OQW 自定义规则；非官方综合评级"},
    }


def build_radar_data(score: dict) -> dict:
    """返回 ECharts radar 配置；数据缺失时不画虚构的闭合六维多边形。"""
    dimensions = score["dimension_scores"]
    missing = [key for key in DIMENSION_LABELS if dimensions[key] is None]
    data = (
        []
        if missing
        else [
            {
                "name": "OQW 绿色指标",
                "value": [dimensions[key] for key in DIMENSION_LABELS],
            }
        ]
    )
    return {
        "radar": {
            "indicator": [{"name": label, "max": 100} for label in DIMENSION_LABELS.values()]
        },
        "series": [{"type": "radar", "data": data}],
        "missing_dimensions": missing,
        "dimension_scores": dict(dimensions),
    }
