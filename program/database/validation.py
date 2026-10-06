"""CSV/JSON 入库校验：未知字段报错，缺列保留原值，显式空值清空。"""

import json
import math
import re
from datetime import date

from chem_engine.hsp_matcher import _cas
from chem_engine.metrics import molecular_weight

SOLVENT_FIELDS = {
    "cas",
    "name",
    "smiles",
    "boiling_point",
    "flash_point",
    "delta_d",
    "delta_p",
    "delta_h",
    "hsp_temperature_c",
    "ghs_codes",
    "gsk_score",
    "raw_scores",
    "excluded",
}
HAZARD_FIELDS = {
    "cas",
    "name",
    "rule_code",
    "rule_type",
    "severity",
    "warning",
    "conditions",
    "is_svhc",
    "exclude_from_recommendations",
    "active",
    "effective_from",
    "effective_to",
}


def strict_json(text: str):
    """拒绝 JSON 重复键和 Python JSON 解码器默认接受的 NaN/Infinity。"""

    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError(f"JSON 存在重复字段: {key}")
            result[key] = value
        return result

    def invalid_constant(value):
        raise ValueError(f"JSON 不接受 {value}")

    result = json.loads(text, object_pairs_hook=pairs, parse_constant=invalid_constant)
    # 1e999 也会被解码为 inf，需要额外进行严格序列化检查。
    json.dumps(result, allow_nan=False)
    return result


def text_value(value, field: str, max_length: int = 10000) -> str:
    if not isinstance(value, str) or not value.strip() or len(value.strip()) > max_length:
        raise ValueError(f"{field} 必须为 1–{max_length} 字符的非空文本")
    return value.strip()


def nullable(value):
    # CSV 空单元格表示 NULL；字符串 'null' 不偷偷转换，避免物质名称被吞掉。
    return None if value is None or (isinstance(value, str) and not value.strip()) else value


def numeric(value, field: str, minimum: float, maximum: float | None = None):
    value = nullable(value)
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float, str)):
        raise ValueError(f"{field} 必须为数字或空值")
    try:
        result = float(value)
    except (ValueError, OverflowError) as exc:
        raise ValueError(f"{field} 不是有效数字") from exc
    if not math.isfinite(result) or result < minimum or (maximum is not None and result > maximum):
        raise ValueError(f"{field} 必须为范围内的有限数字")
    return result


def boolean(value, field: str) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str) and value.strip().lower() in ("true", "false"):
        return value.strip().lower() == "true"
    raise ValueError(f"{field} 只接受 true/false，不接受空值或 0/1")


def normalize_record(record: dict, kind: str, score_method: str | None) -> dict:
    """返回补丁字典。新增时的默认值由 ORM 负责，不污染已有记录。"""
    if not isinstance(record, dict):
        raise ValueError("每条记录必须为对象")
    fields = SOLVENT_FIELDS if kind == "solvents" else HAZARD_FIELDS
    unknown = set(record) - fields
    if unknown:
        raise ValueError(f"未知字段: {', '.join(sorted(unknown))}")
    required = {"cas", "name"}
    if kind == "hazards":
        required |= {"rule_code", "rule_type", "warning"}
    if missing := required - record.keys():
        raise ValueError(f"缺少字段: {', '.join(sorted(missing))}")
    result = dict(record)
    result["cas"] = _cas(record["cas"])
    result["name"] = text_value(record["name"], "name", 200)
    if kind == "solvents":
        if "smiles" in record:
            result["smiles"] = nullable(record["smiles"])
            if result["smiles"] is not None:
                result["smiles"] = text_value(result["smiles"], "smiles")
                molecular_weight(result["smiles"])
        numeric_fields = {
            "boiling_point": -273.15,
            "flash_point": -273.15,
            "hsp_temperature_c": -273.15,
            "delta_d": 0,
            "delta_p": 0,
            "delta_h": 0,
        }
        for field, minimum in numeric_fields.items():
            if field in record:
                result[field] = numeric(record[field], field, minimum)
        hsp_keys = {"delta_d", "delta_p", "delta_h"}
        if hsp_keys & record.keys():
            if not hsp_keys <= record.keys():
                raise ValueError("HSP 三参数必须一起提供，避免不同来源参数混合")
            present = sum(result[key] is not None for key in hsp_keys)
            if present not in (0, 3):
                raise ValueError("HSP 三参数必须全部有值或全部为空")
            # 新 HSP 未提供温度时清除旧温度，不继承另一个来源的测量条件。
            result.setdefault("hsp_temperature_c", None)
        elif "hsp_temperature_c" in record:
            raise ValueError("更新 HSP 温度必须同时提供三参数")
        if "gsk_score" in record:
            result["gsk_score"] = numeric(record["gsk_score"], "gsk_score", 1, 10)
            if result["gsk_score"] is not None and not score_method:
                raise ValueError("提供 gsk_score 时来源配置必须声明 score_method")
            result["score_source"] = score_method if result["gsk_score"] is not None else None
        if "ghs_codes" in record:
            value = nullable(record["ghs_codes"])
            if isinstance(value, str):
                value = strict_json(value) if value.lstrip().startswith("[") else value.split(";")
            if value is not None:
                if not isinstance(value, list) or any(
                    not isinstance(code, str)
                    or not re.fullmatch(r"(?:H\d{3}[A-Za-z]*|EUH\d{3})", code.strip())
                    for code in value
                ):
                    raise ValueError("ghs_codes 应为 H/EUH 代码数组或分号分隔文本")
                value = sorted({code.strip() for code in value})
            result["ghs_codes"] = value
        if "raw_scores" in record:
            value = nullable(record["raw_scores"])
            if isinstance(value, str):
                value = strict_json(value)
            if value is not None and not isinstance(value, dict):
                raise ValueError("raw_scores 必须为对象或空值")
            json.dumps(value, allow_nan=False)
            result["raw_scores"] = value
        if "excluded" in record:
            result["excluded"] = boolean(record["excluded"], "excluded")
    else:
        result["rule_code"] = text_value(record["rule_code"], "rule_code", 100)
        if record["rule_type"] not in (
            "svhc_candidate",
            "authorization",
            "restriction",
            "advisory",
        ):
            raise ValueError("rule_type 必须为 svhc_candidate/authorization/restriction/advisory")
        result["warning"] = text_value(record["warning"], "warning")
        if "severity" in record and record["severity"] not in ("info", "warning", "danger"):
            raise ValueError("severity 必须为 info/warning/danger")
        if "conditions" in record:
            value = nullable(record["conditions"])
            result["conditions"] = None if value is None else text_value(value, "conditions")
        for field in ("is_svhc", "active", "exclude_from_recommendations"):
            if field in record:
                result[field] = boolean(record[field], field)
        if record["rule_type"] == "svhc_candidate":
            if "is_svhc" in result and not result["is_svhc"]:
                raise ValueError("svhc_candidate 记录不能声明 is_svhc=false")
            result["is_svhc"] = True
        for field in ("effective_from", "effective_to"):
            if field in record:
                value = nullable(record[field])
                if value is not None and (
                    not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value)
                ):
                    raise ValueError(f"{field} 必须为 YYYY-MM-DD 或空值")
                result[field] = date.fromisoformat(value) if value else None
    return result
