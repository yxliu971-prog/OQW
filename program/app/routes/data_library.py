"""本机数据中心：上传预览、版本应用、回滚、远程源和计划设置。"""

from typing import Annotated, Literal
from urllib.parse import urlsplit
from uuid import uuid4

from fastapi import APIRouter, Depends, File, Form, Query, Request, UploadFile
from pydantic import BaseModel, ConfigDict, Field, ValidationError
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from database.data_manager import (
    change_dataset,
    commit_upload,
    next_check,
    rollback,
    stage_upload,
    sync_one,
)
from database.dataset_loader import DatasetLoadError
from database.models import DatasetRevision, DatasetSyncRuns, ManagedDataset, SolventData
from database.public_adapters import safe_remote_url

from ..errors import APIError

router = APIRouter(prefix="/datasets", tags=["数据集管理"])


def local_write(request: Request):
    """本机模式写操作需自定义请求头；浏览器跨站表单无法携带该头。"""
    if request.client and request.client.host not in ("127.0.0.1", "::1", "testclient"):
        raise APIError(403, "local_only", "数据管理仅允许本机访问")
    if request.headers.get("X-OQW-Local") != "1":
        raise APIError(403, "local_header_required", "缺少本机管理请求头")
    origin = request.headers.get("origin")
    if origin:
        parts = urlsplit(origin)
        if parts.hostname not in ("localhost", "127.0.0.1", "::1"):
            raise APIError(403, "cross_origin_write", "不允许跨站修改本机数据")


class Metadata(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)
    dataset_id: str | None = Field(default=None, pattern=r"^user-[a-z0-9-]{1,70}$")
    name: str = Field(min_length=1, max_length=200)
    scope: Literal["personal", "local"] = "personal"
    kind: Literal["solvents", "hazards"]
    version: str = Field(min_length=1, max_length=100)
    license: str = Field(min_length=1, max_length=2000)
    attribution: str = Field(min_length=1, max_length=2000)
    region: str = Field(default="", max_length=200)
    score_method: str | None = Field(default=None, max_length=2000)
    format: Literal["csv", "json"]
    column_map: dict[str, str] = Field(default_factory=dict, max_length=50)
    enabled: bool = True
    priority: int = Field(default=100, ge=100, le=999)


class RemoteMetadata(Metadata):
    location: str = Field(max_length=2000)
    interval_hours: int = Field(default=24, ge=0, le=8760)
    jitter_minutes: int = Field(default=0, ge=0, le=1440)


class SettingsPatch(BaseModel):
    model_config = ConfigDict(extra="forbid")
    enabled: bool | None = None
    priority: int | None = Field(default=None, ge=100, le=999)
    interval_hours: int | None = Field(default=None, ge=0, le=8760)
    jitter_minutes: int | None = Field(default=None, ge=0, le=1440)


class RollbackBody(BaseModel):
    model_config = ConfigDict(extra="forbid")
    revision_id: str = Field(min_length=36, max_length=36)


def management_engine(request):
    if request.app.state.settings.allow_demo:
        raise APIError(409, "demo_database", "演示环境不接入正式数据，请切换到正式模式")
    return request.app.state.engine


def handle_error(exc):
    raise APIError(422, "dataset_error", str(exc)) from exc


@router.get("")
def list_datasets(request: Request):
    with Session(request.app.state.engine) as session:
        result = []
        for item in session.scalars(
            select(ManagedDataset).order_by(ManagedDataset.priority, ManagedDataset.id)
        ):
            row = {
                key: getattr(item, key)
                for key in (
                    "id",
                    "name",
                    "scope",
                    "kind",
                    "adapter",
                    "license",
                    "attribution",
                    "region",
                    "score_method",
                    "enabled",
                    "priority",
                    "interval_hours",
                    "jitter_minutes",
                    "next_check_at",
                    "last_checked_at",
                    "last_success_at",
                    "status",
                    "error",
                    "current_revision",
                    "consecutive_failures",
                )
            }
            # UI 只显示不含查询令牌的源地址。
            row["location"] = item.location.split("?")[0]
            revision = (
                session.get(DatasetRevision, item.current_revision)
                if item.current_revision
                else None
            )
            row.update(
                record_count=len(revision.records) if revision else 0,
                version=revision.version if revision else None,
                notes=revision.notes if revision else [],
            )
            result.append(row)
        return {
            "items": result,
            "auto_updates_running": request.app.state.settings.auto_update,
            "demo": request.app.state.settings.allow_demo,
            "solvent_count": session.scalar(select(func.count()).select_from(SolventData)),
        }


@router.get("/history")
def history(request: Request, source_id: str | None = None):
    with Session(request.app.state.engine) as session:
        query = select(DatasetSyncRuns).order_by(DatasetSyncRuns.started_at.desc()).limit(50)
        if source_id:
            query = (
                select(DatasetSyncRuns)
                .where(DatasetSyncRuns.source_id == source_id)
                .order_by(DatasetSyncRuns.started_at.desc())
                .limit(50)
            )
        return [
            {
                key: getattr(row, key)
                for key in (
                    "id",
                    "source_id",
                    "status",
                    "started_at",
                    "finished_at",
                    "inserted",
                    "updated",
                    "unchanged",
                    "error",
                )
            }
            for row in session.scalars(query)
        ]


@router.get("/{identifier}/revisions")
def revisions(identifier: str, request: Request):
    with Session(request.app.state.engine) as session:
        rows = session.scalars(
            select(DatasetRevision)
            .where(DatasetRevision.dataset_id == identifier)
            .order_by(DatasetRevision.created_at.desc())
            .limit(30)
        )
        return [
            {
                "id": row.id,
                "version": row.version,
                "created_at": row.created_at,
                "record_count": len(row.records),
                "sha256": row.sha256,
            }
            for row in rows
        ]


@router.get("/{identifier}/records")
def records(
    identifier: str,
    request: Request,
    offset: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
):
    with Session(request.app.state.engine) as session:
        item = session.get(ManagedDataset, identifier)
        revision = (
            session.get(DatasetRevision, item.current_revision)
            if item and item.current_revision
            else None
        )
        if revision is None:
            raise APIError(404, "no_snapshot", "该数据源尚无成功快照")
        return {
            "total": len(revision.records),
            "items": revision.records[offset : offset + limit],
            "notes": revision.notes,
        }


@router.post("/preview", dependencies=[Depends(local_write)])
async def preview(
    request: Request, file: Annotated[UploadFile, File()], metadata: Annotated[str, Form()]
):
    engine = management_engine(request)
    try:
        model = Metadata.model_validate_json(metadata)
        payload = await file.read(2 * 1024 * 1024 + 1)
        if len(payload) > 2 * 1024 * 1024:
            raise APIError(413, "dataset_too_large", "数据文件超过 2 MiB")
        return stage_upload(engine, model.model_dump(), payload)
    except (ValidationError, ValueError, DatasetLoadError) as exc:
        handle_error(exc)
    finally:
        await file.close()


@router.post("/commit/{preview_id}", dependencies=[Depends(local_write)])
def commit(preview_id: str, request: Request):
    try:
        return commit_upload(management_engine(request), preview_id)
    except DatasetLoadError as exc:
        handle_error(exc)


@router.post("/remote", dependencies=[Depends(local_write)])
def create_remote(payload: RemoteMetadata, request: Request):
    engine = management_engine(request)
    try:
        safe_remote_url(payload.location)
        values = payload.model_dump(exclude={"version", "dataset_id"})
        # 远程来源初次登记为停用，先同步与查看快照再显式启用。
        values["enabled"] = False
        with Session(engine) as session, session.begin():
            item = ManagedDataset(id="user-" + uuid4().hex[:16], adapter="remote", **values)
            session.add(item)
            session.flush()
            item.next_check_at = next_check(item)
            return {
                "id": item.id,
                "enabled": False,
                "message": "已登记；请先更新并检查快照，再启用",
            }
    except (ValueError, OSError) as exc:
        handle_error(exc)


@router.post("/{identifier}/sync", dependencies=[Depends(local_write)])
def sync(identifier: str, request: Request):
    try:
        return sync_one(management_engine(request), identifier)
    except DatasetLoadError as exc:
        handle_error(exc)


@router.patch("/{identifier}", dependencies=[Depends(local_write)])
def settings(identifier: str, payload: SettingsPatch, request: Request):
    try:
        change_dataset(
            management_engine(request),
            identifier,
            payload.model_dump(exclude_none=True, exclude_unset=True),
        )
        return {"status": "saved"}
    except DatasetLoadError as exc:
        handle_error(exc)


@router.post("/{identifier}/rollback", dependencies=[Depends(local_write)])
def revert(identifier: str, payload: RollbackBody, request: Request):
    try:
        rollback(management_engine(request), identifier, payload.revision_id)
        return {"status": "rolled_back", "automatic_update": "paused"}
    except DatasetLoadError as exc:
        handle_error(exc)
