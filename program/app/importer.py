"""配方 CSV 适配：每行一个反应，字段与公开溶剂 CSV 分开。"""

import csv
import io

from database.validation import strict_json

from .errors import APIError

REQUIRED = {"reactants_smiles", "reactants_masses", "product_smiles", "product_mass"}
OPTIONAL = {
    "record_id",
    "reactant_coefficients",
    "product_coefficient",
    "mass_unit",
    "solvent_cas",
    "solvent_name",
    "solvent_mass",
    "solvents_json",
    "total_waste_mass",
    "waste_boundary",
    "energy_score",
    "energy_basis",
    "process_safety_score",
    "process_safety_basis",
}


def parse_csv(payload: bytes, max_rows: int) -> list[tuple[int, dict]]:
    try:
        reader = csv.DictReader(io.StringIO(payload.decode("utf-8-sig"), newline=""), strict=True)
        fields = reader.fieldnames
        if (
            not fields
            or len(fields) != len(set(fields))
            or not REQUIRED <= set(fields)
            or set(fields) - REQUIRED - OPTIONAL
        ):
            raise APIError(
                400,
                "invalid_csv_header",
                "表头重复、缺少必需字段或包含未知字段",
                {"required": sorted(REQUIRED), "optional": sorted(OPTIONAL)},
            )
        rows = []
        for row in reader:
            if None in row or any(value is None for value in row.values()):
                raise APIError(
                    400, "invalid_csv_structure", f"CSV 第 {reader.line_num} 行列数不一致"
                )
            rows.append((reader.line_num, row))
            if len(rows) > max_rows:
                raise APIError(413, "too_many_rows", f"每次最多导入 {max_rows} 行")
        if not rows:
            raise APIError(400, "empty_csv", "CSV 没有数据行")
        return rows
    except (UnicodeError, csv.Error) as exc:
        raise APIError(400, "invalid_csv", "CSV 必须为 UTF-8 编码且符合 CSV 转义格式") from exc


def row_to_request(row: dict, persist: bool) -> dict:
    smiles = row["reactants_smiles"].split(";")
    masses = row["reactants_masses"].split(";")
    coefficients = row.get("reactant_coefficients", "").strip()
    coefficients = coefficients.split(";") if coefficients else [1.0] * len(smiles)
    if len(smiles) != len(masses) or len(smiles) != len(coefficients):
        raise ValueError("反应物 SMILES、质量和系数数量必须一致，以分号分隔")
    result = {
        "reactants": [
            {"smiles": value, "mass": float(mass), "coefficient": float(coefficient)}
            for value, mass, coefficient in zip(smiles, masses, coefficients, strict=True)
        ],
        "product": {
            "smiles": row["product_smiles"],
            "mass": float(row["product_mass"]),
            "coefficient": float(row.get("product_coefficient") or 1),
        },
        "mass_unit": row.get("mass_unit") or "g",
        "persist": persist,
    }
    if row.get("total_waste_mass", "").strip():
        result["total_waste_mass"] = float(row["total_waste_mass"])
    if row.get("waste_boundary", "").strip():
        result["waste_boundary"] = row["waste_boundary"]
    if row.get("solvents_json", "").strip():
        if any(
            row.get(field, "").strip() for field in ("solvent_cas", "solvent_name", "solvent_mass")
        ):
            raise ValueError("solvents_json 不能与单溶剂字段同时使用")
        result["solvents"] = strict_json(row["solvents_json"])
    elif any(
        row.get(field, "").strip() for field in ("solvent_cas", "solvent_name", "solvent_mass")
    ):
        solvent = {
            field.removeprefix("solvent_"): row[field]
            for field in ("solvent_cas", "solvent_name")
            if row.get(field, "").strip()
        }
        if row.get("solvent_mass", "").strip():
            solvent["mass"] = float(row["solvent_mass"])
        result["solvents"] = [solvent]
    for prefix, target in (
        ("energy", "energy_assessment"),
        ("process_safety", "process_safety_assessment"),
    ):
        if row.get(f"{prefix}_score", "").strip() or row.get(f"{prefix}_basis", "").strip():
            result[target] = {
                "score": float(row[f"{prefix}_score"]),
                "basis": row.get(f"{prefix}_basis", ""),
            }
    return result
