"""只同步服务器已配置的来源，不接受任意客户端路径或 URL。"""

from fastapi import APIRouter, Depends, Request, Response

from database.scheduler import sync_sources

from ..dependencies import require_sync_admin
from ..errors import APIError
from ..schemas import SyncRequest, SyncResponse

router = APIRouter(tags=["公开数据同步"])


@router.post(
    "/sync-public-datasets",
    response_model=SyncResponse,
    dependencies=[Depends(require_sync_admin)],
    summary="触发已配置公开数据源的同步",
    responses={207: {"model": SyncResponse}, 502: {"model": SyncResponse}},
)
def sync_public_datasets(payload: SyncRequest, request: Request, response: Response):
    app = request.app
    configured = app.state.sources
    if not configured:
        raise APIError(503, "no_dataset_sources", "尚未配置 OQW_SOURCES_CONFIG")
    identifiers = payload.source_ids if payload.source_ids is not None else list(configured)
    if missing := sorted(set(identifiers) - configured.keys()):
        raise APIError(
            404, "unknown_source_id", "数据源编号未在服务器配置", {"source_ids": missing}
        )
    if not app.state.sync_lock.acquire(blocking=False):
        raise APIError(409, "sync_in_progress", "当前进程已有同步任务，请稍后重试")
    try:
        results = sync_sources(
            app.state.engine,
            [configured[key] for key in identifiers],
            allow_demo=app.state.settings.allow_demo,
        )
    finally:
        app.state.sync_lock.release()
    failed = sum(item["status"] == "failed" for item in results)
    status = "success"
    if failed:
        status = "failed" if failed == len(results) else "partial"
        response.status_code = 502 if status == "failed" else 207
    return {"status": status, "results": results}
