"""公共数值校验：拒绝布尔值、字符串、NaN、无穷大及越界值。"""

import math
from numbers import Real


def number(
    value: Real,
    name: str,
    *,
    minimum: float | None = None,
    maximum: float | None = None,
    positive: bool = False,
) -> float:
    """将有限实数规范化为 float；业务输入错误统一抛出 ValueError。"""
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{name} 必须为有限实数，不能是布尔值或字符串")
    try:
        result = float(value)
    except (OverflowError, ValueError) as exc:
        raise ValueError(f"{name} 超出浮点数范围") from exc
    if not math.isfinite(result):
        raise ValueError(f"{name} 必须为有限实数")
    if positive and result <= 0:
        raise ValueError(f"{name} 必须大于 0")
    if minimum is not None and result < minimum:
        raise ValueError(f"{name} 不能小于 {minimum}")
    if maximum is not None and result > maximum:
        raise ValueError(f"{name} 不能大于 {maximum}")
    return result
