"""基于汉森溶解度参数的确定性替代候选排序。

Ra 单位为 MPa**0.5，越小表示参数越相似。这里只筛选绿色得分严格
更高的候选，不把 HSP 接近视为反应兼容、无毒或可直接替换的证明。
"""

import math
import re
from copy import deepcopy

from ._validation import number


def _cas(value: str) -> str:
    """规范 CAS 格式并验证校验位；这不能证明号码已实际登记。"""
    if not isinstance(value, str) or not re.fullmatch(r"[1-9]\d{1,6}-\d{2}-\d", value.strip()):
        raise ValueError("CAS 必须采用标准格式，例如 67-64-1")
    result = value.strip()
    digits = result.replace("-", "")
    checksum = sum(index * int(digit) for index, digit in enumerate(reversed(digits[:-1]), 1))
    if checksum % 10 != int(digits[-1]):
        raise ValueError(f"CAS 校验位错误: {result}")
    return result


def calculate_hsp_distance(
    delta_d1: float,
    delta_p1: float,
    delta_h1: float,
    delta_d2: float,
    delta_p2: float,
    delta_h2: float,
) -> float:
    """Ra = √[4(δD1−δD2)² + (δP1−δP2)² + (δH1−δH2)²]。

    输入均为同温度、同单位 MPa**0.5 的非负有限参数。
    使用 hypot 避免直接平方造成不必要的数值溢出。
    """
    values = [
        number(value, name, minimum=0)
        for name, value in zip(
            ("delta_d1", "delta_p1", "delta_h1", "delta_d2", "delta_p2", "delta_h2"),
            (delta_d1, delta_p1, delta_h1, delta_d2, delta_p2, delta_h2),
            strict=True,
        )
    ]
    d1, p1, h1, d2, p2, h2 = values
    return number(math.hypot(2 * (d1 - d2), p1 - p2, h1 - h2), "HSP 距离", minimum=0)


def _validate_record(record: dict, index: int) -> dict:
    if not isinstance(record, dict):
        raise ValueError(f"hsp_db[{index}] 必须为字典")
    required = {"cas", "name", "delta_d", "delta_p", "delta_h", "gsk_score"}
    missing = required - record.keys()
    if missing:
        raise ValueError(f"hsp_db[{index}] 缺少字段: {', '.join(sorted(missing))}")
    result = deepcopy(record)
    result["cas"] = _cas(record["cas"])
    if not isinstance(record["name"], str) or not record["name"].strip():
        raise ValueError(f"hsp_db[{index}].name 必须为非空字符串")
    result["name"] = record["name"].strip()
    for field in ("delta_d", "delta_p", "delta_h"):
        result[field] = number(record[field], f"hsp_db[{index}].{field}", minimum=0)
    result["gsk_score"] = number(record["gsk_score"], "gsk_score", minimum=1, maximum=10)
    # gsk_score 是上游已归一化、同口径的等级，不在这里猜测/聚合 GSK 原始分类。
    for field in ("boiling_point", "flash_point", "hsp_temperature_c"):
        value = record.get(field)
        result[field] = None if value is None else number(value, field, minimum=-273.15)
    excluded = record.get("excluded", False)
    if not isinstance(excluded, bool):
        raise ValueError("excluded 必须为布尔值")
    result["excluded"] = excluded
    for field in ("source", "score_source"):
        value = record.get(field)
        if value is not None and (not isinstance(value, str) or not value.strip()):
            raise ValueError(f"{field} 必须为非空字符串或 None")
        result[field] = value.strip() if isinstance(value, str) else None
    return result


def _comparison(target: dict, candidate: dict, field: str) -> dict:
    before, after = target[field], candidate[field]
    return {
        "original": before,
        "replacement": after,
        "difference": None if before is None or after is None else after - before,
        "unit": "°C",
    }


def find_green_replacements(
    target_solvent_cas: str, hsp_db: list[dict], top_k: int = 3
) -> list[dict]:
    """按绿色等级提升过滤，然后按 Ra 升序返回前 top_k 个候选。

    必需字段：cas/name/delta_d/delta_p/delta_h/gsk_score。
    可选字段：boiling_point/flash_point（°C）、source/score_source、
    hsp_temperature_c（°C）、excluded（上游规则矩阵的硬性排除标记）。
    每个 CAS 只允许出现一次；无候选返回 []，目标不存在或数据非法报错。
    并列顺序为绿色得分降序、CAS 升序，保证结果不依赖数据库行顺序。
    明确标注了不同温度或不同评分口径的记录不会混合排序。
    """
    target_cas = _cas(target_solvent_cas)
    if isinstance(top_k, bool) or not isinstance(top_k, int) or top_k < 0:
        raise ValueError("top_k 必须为大于等于 0 的整数")
    if not isinstance(hsp_db, list):
        raise ValueError("hsp_db 必须为字典列表")
    records = [_validate_record(record, index) for index, record in enumerate(hsp_db)]
    by_cas = {}
    for record in records:
        if record["cas"] in by_cas:
            raise ValueError(f"数据库中存在重复 CAS: {record['cas']}")
        by_cas[record["cas"]] = record
    if target_cas not in by_cas:
        raise ValueError(f"数据库中不存在目标溶剂: {target_cas}")
    target = by_cas[target_cas]
    candidates = []
    for candidate in records:
        if candidate["cas"] == target_cas or candidate["excluded"]:
            continue
        if candidate["gsk_score"] <= target["gsk_score"]:
            continue
        source_before, source_after = target["score_source"], candidate["score_source"]
        if source_before is not None and source_after is not None and source_before != source_after:
            continue
        temp_before, temp_after = target["hsp_temperature_c"], candidate["hsp_temperature_c"]
        if (
            temp_before is not None
            and temp_after is not None
            and not math.isclose(temp_before, temp_after, abs_tol=1e-6, rel_tol=0)
        ):
            continue
        distance = calculate_hsp_distance(
            target["delta_d"],
            target["delta_p"],
            target["delta_h"],
            candidate["delta_d"],
            candidate["delta_p"],
            candidate["delta_h"],
        )
        warnings = ["HSP 相似性仅用于候选筛选；仍需核验反应兼容性及具体危害。"]
        if target["source"] is None or candidate["source"] is None:
            warnings.append("目标或候选缺少数据来源，尚未完成来源核验。")
        if source_before is None or source_after is None:
            warnings.append("评分口径未完整记录；暂按输入等级可比处理。")
        if temp_before is None or temp_after is None:
            warnings.append("HSP 测量温度未完整记录；暂按同温度处理。")
        candidates.append(
            {
                "cas": candidate["cas"],
                "name": candidate["name"],
                "hsp_distance": distance,
                "hsp_distance_unit": "MPa^0.5",
                "gsk_score": candidate["gsk_score"],
                "original_gsk_score": target["gsk_score"],
                "green_score_change": candidate["gsk_score"] - target["gsk_score"],
                "boiling_point_comparison": _comparison(target, candidate, "boiling_point"),
                "flash_point_comparison": _comparison(target, candidate, "flash_point"),
                "source": candidate["source"],
                "score_source": candidate["score_source"],
                "original_source": target["source"],
                "original_score_source": target["score_source"],
                "hsp_temperature_c": candidate["hsp_temperature_c"],
                "original_hsp_temperature_c": target["hsp_temperature_c"],
                "warnings": warnings,
            }
        )
    candidates.sort(key=lambda item: (item["hsp_distance"], -item["gsk_score"], item["cas"]))
    return candidates[:top_k]
