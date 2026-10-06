"""本地文件/HTTP 数据加载。只同步公开数据表，按来源记录审计。"""

import csv
import hashlib
import io
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
from uuid import uuid4

import httpx
from sqlalchemy import Engine, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from .models import DatasetBaseline, DatasetSyncRuns, HazardRules, SolventData, utc_now
from .validation import normalize_record, strict_json, text_value


class DatasetLoadError(ValueError):
    """可供 CLI / 后续 API 层展示的加载失败。"""


@dataclass(frozen=True)
class DatasetSource:
    """一个受信任的本地/远程来源；格式与单位必须明确，不猜测评分方向。"""

    source_id: str
    location: str
    format: str
    version: str
    license: str
    kind: str = "solvents"
    attribution: str = ""
    score_method: str | None = None
    hsp_unit: str = "MPa^0.5"
    temperature_unit: str = "C"
    records_key: str | None = None
    column_map: dict[str, str] = field(default_factory=dict)
    is_demo: bool = False
    expected_sha256: str | None = None
    max_bytes: int = 10 * 1024 * 1024
    max_rows: int = 50000
    timeout_seconds: float = 30

    def __post_init__(self):
        if not isinstance(self.source_id, str) or not re.fullmatch(
            r"[A-Za-z0-9_.-]{1,100}", self.source_id
        ):
            raise ValueError("source_id 必须为 1–100 位字母、数字、点、横线或下划线")
        text_value(self.location, "location")
        text_value(self.version, "version", 100)
        text_value(self.license, "license")
        if self.kind not in ("solvents", "hazards") or self.format not in ("csv", "json"):
            raise ValueError("kind 必须为 solvents/hazards，format 必须为 csv/json")
        if self.hsp_unit != "MPa^0.5" or self.temperature_unit != "C":
            raise ValueError("请先将 HSP 转换为 MPa^0.5、温度转换为 C 后再导入")
        if self.score_method is not None:
            text_value(self.score_method, "score_method")
        if self.records_key is not None:
            text_value(self.records_key, "records_key")
        if self.format == "csv" and self.records_key is not None:
            raise ValueError("CSV 不接受 records_key")
        if not isinstance(self.column_map, dict) or any(
            not isinstance(key, str) or not isinstance(value, str) or not key or not value
            for key, value in self.column_map.items()
        ):
            raise ValueError("column_map 必须为 原始字段:标准字段 的字典")
        if len(set(self.column_map.values())) != len(self.column_map):
            raise ValueError("column_map 不能将多个字段映射到同一个字段")
        if not isinstance(self.is_demo, bool):
            raise ValueError("is_demo 必须为布尔值")
        for name in ("max_bytes", "max_rows"):
            value = getattr(self, name)
            if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
                raise ValueError(f"{name} 必须为正整数")
        if (
            isinstance(self.timeout_seconds, bool)
            or not isinstance(self.timeout_seconds, (int, float))
            or not 0 < self.timeout_seconds <= 300
        ):
            raise ValueError("timeout_seconds 必须为 0–300 秒范围内的正数")
        if self.expected_sha256 is not None and not re.fullmatch(
            r"[a-f0-9]{64}", self.expected_sha256
        ):
            raise ValueError("expected_sha256 必须为 64 位小写十六进制")
        if "://" in self.location:
            url = urlsplit(self.location)
            if (
                url.scheme not in ("https", "http")
                or not url.netloc
                or url.username
                or url.password
                or url.fragment
            ):
                raise ValueError("仅接受无用户密码、无片段的 HTTP(S) URL")

    def provenance(self) -> dict:
        # 查询参数可能含访问令牌，不存进数据库日志。请求仍使用完整配置 URL。
        location = self.location
        if "://" in location:
            url = urlsplit(location)
            location = urlunsplit((url.scheme, url.netloc, url.path, "", ""))
        return {
            "source_id": self.source_id,
            "location": location,
            "version": self.version,
            "license": self.license,
            "attribution": self.attribution,
            "score_method": self.score_method,
            "hsp_unit": self.hsp_unit,
            "temperature_unit": self.temperature_unit,
            "is_demo": self.is_demo,
        }


@dataclass(frozen=True)
class SyncResult:
    run_id: str
    source_id: str
    inserted: int
    updated: int
    unchanged: int
    sha256: str

    def to_dict(self) -> dict:
        return asdict(self)


def _read_payload(source: DatasetSource, client: httpx.Client | None) -> bytes:
    if "://" not in source.location:
        with Path(source.location).open("rb") as file:
            payload = file.read(source.max_bytes + 1)
    else:

        def download(active_client):
            data = bytearray()
            # 不自动跟随重定向，管理员应在配置中显式填写实际数据端点。
            with active_client.stream(
                "GET", source.location, timeout=source.timeout_seconds, follow_redirects=False
            ) as response:
                response.raise_for_status()
                for chunk in response.iter_bytes(chunk_size=65536):
                    data.extend(chunk)
                    if len(data) > source.max_bytes:
                        raise DatasetLoadError("远程响应超过 max_bytes 限制")
            return bytes(data)

        if client is not None:
            payload = download(client)
        else:
            with httpx.Client() as owned_client:
                payload = download(owned_client)
    if len(payload) > source.max_bytes:
        raise DatasetLoadError("文件超过 max_bytes 限制")
    if not payload:
        raise DatasetLoadError("数据源为空")
    return payload


def _parse_payload(payload: bytes, source: DatasetSource) -> list[dict]:
    text = payload.decode("utf-8-sig")
    if source.format == "json":
        records = strict_json(text)
        if source.records_key:
            if not isinstance(records, dict) or source.records_key not in records:
                raise DatasetLoadError(f"JSON 不包含 records_key={source.records_key}")
            records = records[source.records_key]
        if not isinstance(records, list):
            raise DatasetLoadError("JSON 必须为记录数组，或配置 records_key 提取数组")
    else:
        reader = csv.DictReader(io.StringIO(text, newline=""), strict=True)
        fields = reader.fieldnames
        if (
            not fields
            or len(fields) != len(set(fields))
            or any(not value.strip() for value in fields)
        ):
            raise DatasetLoadError("CSV 表头不能为空或重复")
        records = []
        for record in reader:
            if None in record or any(value is None for value in record.values()):
                raise DatasetLoadError(f"CSV 第 {reader.line_num} 行列数与表头不一致")
            records.append(record)
            if len(records) > source.max_rows:
                raise DatasetLoadError("记录数超过 max_rows 限制")
    if not records or len(records) > source.max_rows:
        raise DatasetLoadError("数据数组不能为空，且不能超过 max_rows")
    normalized = []
    seen = set()
    for index, record in enumerate(records, start=1):
        try:
            if not isinstance(record, dict):
                raise ValueError("记录必须为对象")
            renamed = {}
            for key, value in record.items():
                name = source.column_map.get(key, key)
                if name in renamed:
                    raise ValueError(f"字段映射冲突: {name}")
                renamed[name] = value
            row = normalize_record(renamed, source.kind, source.score_method)
            key = row["cas"] if source.kind == "solvents" else (row["cas"], row["rule_code"])
            if key in seen:
                raise ValueError("同一批次出现重复 CAS / 规则键")
            seen.add(key)
            normalized.append(row)
        except (ValueError, TypeError) as exc:
            raise DatasetLoadError(f"第 {index} 条记录: {exc}") from exc
    return normalized


def _apply_rows(session: Session, source: DatasetSource, rows: list[dict]) -> tuple[int, int, int]:
    inserted = updated = unchanged = 0
    provenance = source.provenance()
    for row in rows:
        if source.kind == "solvents":
            obj = session.scalar(
                select(SolventData).where(SolventData.cas == row["cas"]).with_for_update()
            )
            new = obj is None
            if new:
                obj = SolventData(**row, is_demo=source.is_demo, field_sources={})
                session.add(obj)
            elif obj.is_demo != source.is_demo:
                raise DatasetLoadError("禁止混合演示数据和生产数据，请使用独立数据库")
            field_sources = dict(obj.field_sources)
            changed = new
            for key, value in row.items():
                if getattr(obj, key) != value or field_sources.get(key) != provenance:
                    changed = True
                setattr(obj, key, value)
                field_sources[key] = provenance
            if changed:
                obj.field_sources = field_sources
        else:
            obj = session.scalar(
                select(HazardRules)
                .where(
                    HazardRules.cas == row["cas"],
                    HazardRules.rule_code == row["rule_code"],
                    HazardRules.source_id == source.source_id,
                )
                .with_for_update()
            )
            new = obj is None
            if new:
                obj = HazardRules(
                    **row, source_id=source.source_id, provenance=provenance, is_demo=source.is_demo
                )
                session.add(obj)
            elif obj.is_demo != source.is_demo:
                raise DatasetLoadError("禁止混合演示和生产危害规则")
            changed = (
                new
                or obj.provenance != provenance
                or any(getattr(obj, key) != value for key, value in row.items())
            )
            for key, value in row.items():
                setattr(obj, key, value)
            if obj.effective_from and obj.effective_to and obj.effective_from > obj.effective_to:
                raise DatasetLoadError("危害规则 effective_from 不能晚于 effective_to")
            if changed:
                obj.provenance = provenance
        if new:
            inserted += 1
        elif changed:
            updated += 1
        else:
            unchanged += 1
    session.flush()
    return inserted, updated, unchanged


def sync_dataset(
    engine: Engine,
    source: DatasetSource,
    *,
    allow_demo: bool = False,
    client: httpx.Client | None = None,
) -> SyncResult:
    """整批 upsert：缺少字段保留，显式 null 清空；不删除源中缺席的记录。

    已成功导入相同内容仍会校验并执行比较，返回 unchanged 并记录检查时间。
    engine 的表须先用 initialize_database 初始化。一次调用对应一个事务。
    """
    started_at = utc_now()
    run_id = str(uuid4())
    checksum = None
    provenance = source.provenance()
    common = dict(
        id=run_id,
        source_id=source.source_id,
        dataset_kind=source.kind,
        source_version=source.version,
        source_location=provenance["location"],
        started_at=started_at,
        provenance=provenance,
    )
    try:
        with Session(engine) as guard:
            if guard.get(DatasetBaseline, 1) is not None:
                raise DatasetLoadError(
                    "该库已由数据中心接管，请在数据集管理页面更新，避免绕过版本与覆盖层"
                )
        if source.is_demo and not allow_demo:
            raise DatasetLoadError("演示数据需显式 allow_demo=True / --allow-demo")
        payload = _read_payload(source, client)
        checksum = hashlib.sha256(payload).hexdigest()
        if source.expected_sha256 and checksum != source.expected_sha256:
            raise DatasetLoadError("数据 SHA-256 与配置不一致")
        rows = _parse_payload(payload, source)
        with Session(engine) as session, session.begin():
            inserted, updated, unchanged = _apply_rows(session, source, rows)
            session.add(
                DatasetSyncRuns(
                    **common,
                    status="success",
                    sha256=checksum,
                    inserted=inserted,
                    updated=updated,
                    unchanged=unchanged,
                )
            )
        return SyncResult(run_id, source.source_id, inserted, updated, unchanged, checksum)
    except (ValueError, TypeError, OSError, csv.Error, httpx.HTTPError, SQLAlchemyError) as exc:
        # HTTP 异常文本可能带 URL 查询令牌，数据库异常可能带整条参数，均不写入审计。
        if isinstance(exc, httpx.HTTPError):
            message = f"远程请求失败: {type(exc).__name__}"
        elif isinstance(exc, SQLAlchemyError):
            message = f"数据库事务失败: {type(exc).__name__}；本批数据已回滚"
        else:
            message = str(exc)[:2000]
        try:
            with Session(engine) as session, session.begin():
                session.add(
                    DatasetSyncRuns(**common, status="failed", sha256=checksum, error=message)
                )
        except SQLAlchemyError as audit_exc:
            raise DatasetLoadError(f"{message}；失败审计也无法写入，请检查数据库") from audit_exc
        raise DatasetLoadError(message) from exc


def load_source_config(config_path: str | Path) -> list[DatasetSource]:
    """配置中的本地相对路径按配置文件目录解析，而不是终端工作目录。"""
    path = Path(config_path).resolve()
    config = strict_json(path.read_text(encoding="utf-8-sig"))
    if (
        not isinstance(config, dict)
        or set(config) != {"sources"}
        or not isinstance(config["sources"], list)
        or not config["sources"]
    ):
        raise ValueError("配置必须为包含非空 sources 数组的对象")
    sources = []
    identifiers = set()
    for item in config["sources"]:
        if not isinstance(item, dict):
            raise ValueError("sources 每项必须为对象")
        values = dict(item)
        source = DatasetSource(**values)
        if "://" not in source.location:
            values["location"] = str((path.parent / source.location).resolve())
            source = DatasetSource(**values)
        if source.source_id in identifiers:
            raise ValueError("来源配置中 source_id 重复")
        identifiers.add(source.source_id)
        sources.append(source)
    return sources
