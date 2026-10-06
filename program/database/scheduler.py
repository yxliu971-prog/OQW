"""显式启动的前台定期同步；导入模块不创建线程或系统计划任务。"""

import math
from collections.abc import Iterator, Sequence
from threading import Event

from sqlalchemy import Engine

from .dataset_loader import DatasetLoadError, DatasetSource, sync_dataset


def sync_sources(
    engine: Engine, sources: Sequence[DatasetSource], *, allow_demo: bool = False
) -> list[dict]:
    """每个数据源独立事务；某个来源失败不阻塞其他来源，结果明确标注失败。"""
    results = []
    for source in sources:
        try:
            result = sync_dataset(engine, source, allow_demo=allow_demo)
            results.append({"status": "success", **result.to_dict()})
        except DatasetLoadError as exc:
            results.append({"status": "failed", "source_id": source.source_id, "error": str(exc)})
    return results


def iter_sync_cycles(
    engine: Engine,
    sources: Sequence[DatasetSource],
    *,
    interval_seconds: float = 86400,
    allow_demo: bool = False,
    stop_event: Event | None = None,
    max_cycles: int | None = None,
) -> Iterator[list[dict]]:
    """立即运行一次；完成后等待 interval_seconds，再运行下一次。

    Event.wait 可中断，Ctrl+C 由 CLI 处理。每轮失败会记录并在下轮重试。
    按固定间隔工作，不执行自动 schema 变更，不在用户登录后自动启动。
    """
    if (
        isinstance(interval_seconds, bool)
        or not isinstance(interval_seconds, (int, float))
        or not math.isfinite(interval_seconds)
        or interval_seconds < 60
    ):
        raise ValueError("同步间隔必须为不小于 60 秒的有限数")
    if max_cycles is not None and (
        isinstance(max_cycles, bool) or not isinstance(max_cycles, int) or max_cycles <= 0
    ):
        raise ValueError("max_cycles 必须为正整数或 None")
    if not sources:
        raise ValueError("至少需要一个数据源")
    stop = stop_event if stop_event is not None else Event()
    count = 0
    while not stop.is_set():
        yield sync_sources(engine, sources, allow_demo=allow_demo)
        count += 1
        if max_cycles is not None and count >= max_cycles:
            break
        if stop.wait(interval_seconds):
            break
