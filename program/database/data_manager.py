"""有版本、可回滚的本机数据目录；公开快照和个人覆盖层分开保存。"""

import hashlib
import json
import random
from contextlib import contextmanager
from dataclasses import asdict
from datetime import date, timedelta
from uuid import uuid4

import httpx
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session

from .dataset_loader import DatasetLoadError, DatasetSource, _apply_rows, _parse_payload
from .models import (
    DatasetBaseline,
    DatasetLease,
    DatasetRevision,
    DatasetSyncRuns,
    HazardRules,
    ManagedDataset,
    SolventData,
    utc_now,
)
from .public_adapters import CATALOG, Download, download


def json_safe(value):
    return json.loads(json.dumps(value, ensure_ascii=False, default=lambda x: x.isoformat()))


def register_catalog(engine):
    with Session(engine) as session, session.begin():
        if session.get(DatasetLease, 1) is None:
            session.add(DatasetLease(id=1))
        for config in CATALOG:
            if session.get(ManagedDataset, config["id"]) is None:
                # 首次加载只登记；明确启用数据服务后由调度线程拉取。
                session.add(ManagedDataset(**config, scope="public", next_check_at=utc_now()))


@contextmanager
def lease(engine):
    owner = str(uuid4())
    now = utc_now()
    with Session(engine) as session, session.begin():
        row = session.execute(
            update(DatasetLease)
            .where(
                DatasetLease.id == 1,
                (DatasetLease.owner.is_(None)) | (DatasetLease.expires_at < now),
            )
            .values(owner=owner, expires_at=now + timedelta(minutes=30))
        )
        if row.rowcount != 1:
            raise DatasetLoadError("已有数据更新正在执行，请稍后重试")
    try:
        yield
    finally:
        with Session(engine) as session, session.begin():
            session.execute(
                update(DatasetLease)
                .where(DatasetLease.id == 1, DatasetLease.owner == owner)
                .values(owner=None, expires_at=None)
            )


def serialize_model(obj):
    return json_safe(
        {
            column.name: getattr(obj, column.name)
            for column in obj.__table__.columns
            if column.name not in ("id", "created_at", "updated_at")
        }
    )


def baseline(session):
    record = session.get(DatasetBaseline, 1)
    if record is None:
        solvents = list(session.scalars(select(SolventData)))
        hazards = list(session.scalars(select(HazardRules)))
        if any(item.is_demo for item in solvents + hazards):
            raise DatasetLoadError("演示库不能接入正式数据，请使用不带 --demo 的正式工作台")
        record = DatasetBaseline(
            id=1,
            solvents=[serialize_model(x) for x in solvents],
            hazards=[serialize_model(x) for x in hazards],
        )
        session.add(record)
        session.flush()
    return record


def source_for(item, version, *, location=None):
    return DatasetSource(
        source_id=item.id,
        location=location or item.location or "local-upload",
        format=item.format,
        version=version,
        license=item.license,
        kind=item.kind,
        attribution=item.attribution,
        score_method=item.score_method,
        column_map=item.column_map,
        max_rows=10000,
        max_bytes=2 * 1024 * 1024,
    )


def rebuild(session):
    """在同一事务重建当前视图。停用/撤回高优先级来源后恢复低优先级值。"""
    base = baseline(session)
    session.execute(delete(SolventData))
    session.execute(delete(HazardRules))
    for data in base.solvents:
        session.add(SolventData(**data))
    for data in base.hazards:
        restored = dict(data)
        for key in ("effective_from", "effective_to"):
            if restored.get(key):
                restored[key] = date.fromisoformat(restored[key])
        session.add(HazardRules(**restored))
    session.flush()
    ordered = session.scalars(
        select(ManagedDataset)
        .where(ManagedDataset.enabled.is_(True), ManagedDataset.current_revision.is_not(None))
        .order_by(ManagedDataset.priority, ManagedDataset.id)
    ).all()
    for item in ordered:
        revision = session.get(DatasetRevision, item.current_revision)
        source = DatasetSource(**revision.provenance["source_config"])
        # 快照中存标准字段；移除派生 score_source，由规范化再次生成。
        rows = []
        for record in revision.records:
            row = dict(record)
            row.pop("score_source", None)
            # 部分公共数据只提供 CAS，不能把已知化学名称覆盖成 CAS。
            known = session.scalar(select(SolventData).where(SolventData.cas == row["cas"]))
            if item.kind == "solvents" and known is not None:
                if row["name"] == row["cas"]:
                    row["name"] = known.name
                # 原始分类按来源并存，避免物性同步抹掉 SCIL 分类和备注。
                if isinstance(known.raw_scores, dict) and isinstance(row.get("raw_scores"), dict):
                    row["raw_scores"] = {**known.raw_scores, **row["raw_scores"]}
            rows.append(row)
        parsed = _parse_payload(
            json.dumps(rows, ensure_ascii=False).encode(),
            DatasetSource(**{**asdict(source), "format": "json", "column_map": {}}),
        )
        _apply_rows(session, source, parsed)


def next_check(item, now=None):
    if not item.enabled or not item.interval_hours or item.adapter == "upload":
        return None
    now = now or utc_now()
    hours = item.interval_hours
    # 故障退避：不密集重试，最多 7 天；成功后恢复用户设定的间隔。
    if item.consecutive_failures:
        hours = max(hours, min(168, hours * 2 ** min(item.consecutive_failures - 1, 5)))
    return now + timedelta(hours=hours, minutes=random.uniform(0, item.jitter_minutes))


def validate_records(records, source):
    raw = json.dumps(records, ensure_ascii=False, allow_nan=False).encode()
    parsed = _parse_payload(
        raw, DatasetSource(**{**asdict(source), "format": "json", "column_map": {}})
    )
    for row in parsed:
        if (
            row.get("effective_from")
            and row.get("effective_to")
            and row["effective_from"] > row["effective_to"]
        ):
            raise DatasetLoadError("规则失效日期不能早于生效日期")
    return json_safe(parsed)


def apply_revision(session, item, records, sha256, notes, version, source):
    current = session.get(DatasetRevision, item.current_revision) if item.current_revision else None
    changed = current is None or current.records != records
    if changed:
        # 大规模缩减保护：公开来源若一次减少超过 25%，需要人工检查，旧值仍有效。
        if item.scope == "public" and current and len(records) < len(current.records) * 0.75:
            raise DatasetLoadError("上游记录缩减超过 25%，本次更新拒绝应用，保留旧版本")
        revision = DatasetRevision(
            dataset_id=item.id,
            version=version,
            records=records,
            sha256=sha256,
            provenance={"source_config": asdict(source)},
            notes=notes,
        )
        session.add(revision)
        session.flush()
        item.current_revision = revision.id
        session.flush()
        rebuild(session)
    item.status = "updated" if changed else "unchanged"
    item.error = None
    item.consecutive_failures = 0
    item.last_checked_at = item.last_success_at = utc_now()
    item.next_check_at = next_check(item)
    return changed


def sync_one(engine, identifier, *, client=None, only_if_due=False):
    """请求在事务外完成；解析失败不覆盖旧快照；同步锁跨进程有效。"""
    with lease(engine):
        with Session(engine) as session:
            item = session.get(ManagedDataset, identifier)
            if item is None or item.adapter == "upload":
                raise DatasetLoadError("该数据源不存在或只能通过重新上传更新")
            if only_if_due and (
                not item.enabled
                or not item.interval_hours
                or not item.next_check_at
                or item.next_check_at > utc_now()
            ):
                return {"status": "skipped", "reason": "未到期或已停用"}
            session.expunge(item)
        started = utc_now()
        try:
            fetched = download(item.adapter, item.location, client=client)
            version = started.strftime("%Y%m%dT%H%M%SZ")
            source = source_for(item, version)
            if isinstance(fetched, Download):
                records = validate_records(fetched.records, source)
                checksum, notes = fetched.sha256, fetched.notes
            else:
                records = json_safe(_parse_payload(fetched, source))
                records = validate_records(
                    [{k: v for k, v in r.items() if k != "score_source"} for r in records], source
                )
                checksum, notes = hashlib.sha256(fetched).hexdigest(), []
            version += "-" + checksum[:10]
            source = source_for(item, version)
            with Session(engine) as session, session.begin():
                item = session.get(ManagedDataset, identifier)
                changed = apply_revision(session, item, records, checksum, notes, version, source)
                session.add(
                    DatasetSyncRuns(
                        source_id=item.id,
                        dataset_kind=item.kind,
                        source_version=version,
                        source_location=source.provenance()["location"],
                        status="success",
                        started_at=started,
                        sha256=checksum,
                        updated=len(records) if changed else 0,
                        unchanged=0 if changed else len(records),
                        provenance=source.provenance(),
                    )
                )
            return {"status": "updated" if changed else "unchanged", "record_count": len(records)}
        except Exception as exc:
            if isinstance(exc, httpx.HTTPStatusError):
                message = f"上游返回 HTTP {exc.response.status_code}，旧版本仍保留"
            elif isinstance(exc, httpx.HTTPError):
                message = f"下载失败（{type(exc).__name__}），旧版本仍保留"
            elif isinstance(exc, (ValueError, DatasetLoadError)):
                message = str(exc)[:1200]
            else:
                message = f"更新失败（{type(exc).__name__}），请检查本地日志；旧版本仍保留"
            with Session(engine) as session, session.begin():
                item = session.get(ManagedDataset, identifier)
                item.status, item.error = "failed", message
                item.last_checked_at = utc_now()
                item.consecutive_failures += 1
                item.next_check_at = next_check(item)
                session.add(
                    DatasetSyncRuns(
                        source_id=item.id,
                        dataset_kind=item.kind,
                        source_version="failed-check",
                        source_location=source_for(item, "unknown").provenance()["location"],
                        status="failed",
                        started_at=started,
                        error=message,
                        provenance={"scope": item.scope},
                    )
                )
            raise DatasetLoadError(message) from exc


def stage_upload(engine, metadata, payload):
    identifier = metadata.pop("dataset_id", None) or "user-" + uuid4().hex[:16]
    with Session(engine) as session:
        existing = session.get(ManagedDataset, identifier)
        if existing is not None and existing.scope == "public":
            raise DatasetLoadError("个人上传不能替换公开来源，请创建独立覆盖数据集")
        if existing is not None and existing.kind != metadata["kind"]:
            raise DatasetLoadError("已有数据集不能更换数据类型，请创建新的数据集")
    version = metadata.pop("version")
    item = ManagedDataset(id=identifier, adapter="upload", location="local-upload", **metadata)
    source = source_for(item, version)
    records = json_safe(_parse_payload(payload, source))
    records = validate_records(
        [{k: v for k, v in r.items() if k != "score_source"} for r in records], source
    )
    clean_source = DatasetSource(**{**asdict(source), "format": "json", "column_map": {}})
    with Session(engine) as session, session.begin():
        conflicts = (
            list(
                session.scalars(
                    select(SolventData.cas).where(SolventData.cas.in_([r["cas"] for r in records]))
                )
            )
            if item.kind == "solvents"
            else []
        )
        snapshot = {**metadata, "id": identifier, "adapter": "upload", "location": "local-upload"}
        revision = DatasetRevision(
            dataset_id="pending",
            version=version,
            records=records,
            sha256=hashlib.sha256(payload).hexdigest(),
            provenance={
                "source_config": asdict(clean_source),
                "pending_metadata": snapshot,
                "expected_current": existing.current_revision if existing else None,
            },
            notes=["本机用户上传；来源内容和适用范围由使用者提供，未自动认证。"],
        )
        session.add(revision)
        session.flush()
        return {
            "preview_id": revision.id,
            "dataset_id": identifier,
            "record_count": len(records),
            "sample": records[:8],
            "conflicting_cas": conflicts[:30],
            "conflict_count": len(conflicts),
            "notes": revision.notes,
        }


def commit_upload(engine, preview_id):
    with lease(engine), Session(engine) as session, session.begin():
        revision = session.get(DatasetRevision, preview_id)
        if revision is None or revision.dataset_id != "pending":
            raise DatasetLoadError("预览不存在或已经导入，请重新预览")
        if utc_now() - revision.created_at > timedelta(hours=24):
            raise DatasetLoadError("预览已过期，请重新上传")
        meta = revision.provenance["pending_metadata"]
        item = session.get(ManagedDataset, meta["id"])
        current = item.current_revision if item else None
        if current != revision.provenance["expected_current"]:
            raise DatasetLoadError("预览后数据集已更新，请重新预览，避免覆盖其他修改")
        if item is None:
            item = ManagedDataset(**meta)
            session.add(item)
        else:
            for key, value in meta.items():
                setattr(item, key, value)
        item.current_revision = revision.id
        item.status = "updated"
        item.last_checked_at = item.last_success_at = utc_now()
        item.error = None
        item.interval_hours = item.jitter_minutes = item.consecutive_failures = 0
        item.next_check_at = None
        revision.dataset_id = item.id
        session.flush()
        rebuild(session)
        audit_action(session, item, revision, "upload")
        return {"id": item.id, "record_count": len(revision.records), "revision_id": revision.id}


def change_dataset(engine, identifier, values):
    with lease(engine), Session(engine) as session, session.begin():
        item = session.get(ManagedDataset, identifier)
        if item is None:
            raise DatasetLoadError("数据集不存在")
        if item.scope == "public" and "priority" in values:
            raise DatasetLoadError("公开来源优先级固定，个人/当地覆盖层可以调整优先级")
        if item.adapter == "upload" and values.get("interval_hours", 0):
            raise DatasetLoadError(
                "浏览器上传的文件不能自动读取本地原文件，请重新上传或添加 HTTPS 源"
            )
        for key, value in values.items():
            setattr(item, key, value)
        item.next_check_at = next_check(item)
        if item.current_revision and any(key in values for key in ("enabled", "priority")):
            session.flush()
            rebuild(session)


def rollback(engine, identifier, revision_id):
    with lease(engine), Session(engine) as session, session.begin():
        item = session.get(ManagedDataset, identifier)
        revision = session.get(DatasetRevision, revision_id)
        if item is None or revision is None or revision.dataset_id != identifier:
            raise DatasetLoadError("数据集或指定历史版本不存在")
        item.current_revision = revision.id
        item.status = "rolled_back"
        source = revision.provenance["source_config"]
        for key in ("kind", "license", "attribution", "score_method"):
            setattr(item, key, source[key])
        # 回滚后暂停自动更新，避免下一轮立即覆盖恢复版本。
        item.interval_hours = 0
        item.next_check_at = None
        session.flush()
        rebuild(session)
        audit_action(session, item, revision, "rollback")


def audit_action(session, item, revision, action):
    session.add(
        DatasetSyncRuns(
            source_id=item.id,
            dataset_kind=item.kind,
            source_version=revision.version,
            source_location="local-data-center",
            status="success",
            started_at=utc_now(),
            sha256=revision.sha256,
            updated=len(revision.records),
            provenance={"action": action, "scope": item.scope},
        )
    )


def run_due(engine, stop):
    """服务在运行时每 30 秒检查到期任务；持久化 next_check，重启后补查。"""
    while not stop.is_set():
        with Session(engine) as session:
            due = list(
                session.scalars(
                    select(ManagedDataset.id)
                    .where(
                        ManagedDataset.enabled.is_(True),
                        ManagedDataset.interval_hours > 0,
                        ManagedDataset.next_check_at <= utc_now(),
                    )
                    .order_by(ManagedDataset.priority)
                )
            )
        for identifier in due:
            if stop.is_set():
                break
            try:
                sync_one(engine, identifier, only_if_due=True)
            except DatasetLoadError:
                pass  # 已记录失败与退避，下轮只检查到期来源。
        stop.wait(30)
