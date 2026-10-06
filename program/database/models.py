"""OQW SQLAlchemy 2.0 模型。公开数据同步绝不写入私有评估表。"""

from datetime import date, datetime, timezone
from uuid import uuid4

from sqlalchemy import (
    JSON,
    Boolean,
    CheckConstraint,
    Date,
    DateTime,
    Float,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import TypeDecorator


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class UTCDateTime(TypeDecorator):
    """SQLite 不保留时区；统一存 UTC，读取时补齐 UTC 时区。"""

    impl = DateTime(timezone=True)
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("时间必须包含时区")
        return value.astimezone(timezone.utc)

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        return (
            value.replace(tzinfo=timezone.utc)
            if value.tzinfo is None
            else value.astimezone(timezone.utc)
        )


class Base(DeclarativeBase):
    pass


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(UTCDateTime(), default=utc_now)
    updated_at: Mapped[datetime] = mapped_column(UTCDateTime(), default=utc_now, onupdate=utc_now)


class SolventData(TimestampMixin, Base):
    """当前溶剂快照。未知物性为 NULL，JSON 字段修改时应整体重新赋值。"""

    __tablename__ = "solvent_data"
    __table_args__ = (
        CheckConstraint(
            "gsk_score IS NULL OR (gsk_score >= 1 AND gsk_score <= 10)", name="ck_solvent_score"
        ),
        CheckConstraint("delta_d IS NULL OR delta_d >= 0", name="ck_solvent_d"),
        CheckConstraint("delta_p IS NULL OR delta_p >= 0", name="ck_solvent_p"),
        CheckConstraint("delta_h IS NULL OR delta_h >= 0", name="ck_solvent_h"),
        CheckConstraint(
            "(delta_d IS NULL AND delta_p IS NULL AND delta_h IS NULL) OR "
            "(delta_d IS NOT NULL AND delta_p IS NOT NULL AND delta_h IS NOT NULL)",
            name="ck_hsp_complete",
        ),
        CheckConstraint("boiling_point IS NULL OR boiling_point >= -273.15", name="ck_boiling"),
        CheckConstraint("flash_point IS NULL OR flash_point >= -273.15", name="ck_flash"),
        CheckConstraint(
            "hsp_temperature_c IS NULL OR hsp_temperature_c >= -273.15", name="ck_hsp_temp"
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    cas: Mapped[str] = mapped_column(String(12), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(200), index=True)
    smiles: Mapped[str | None] = mapped_column(Text)
    boiling_point: Mapped[float | None] = mapped_column(Float)
    flash_point: Mapped[float | None] = mapped_column(Float)
    delta_d: Mapped[float | None] = mapped_column(Float)
    delta_p: Mapped[float | None] = mapped_column(Float)
    delta_h: Mapped[float | None] = mapped_column(Float)
    hsp_temperature_c: Mapped[float | None] = mapped_column(Float)
    ghs_codes: Mapped[list | None] = mapped_column(JSON(none_as_null=True))
    gsk_score: Mapped[float | None] = mapped_column(Float)
    raw_scores: Mapped[dict | None] = mapped_column(JSON(none_as_null=True))
    score_source: Mapped[str | None] = mapped_column(Text)
    excluded: Mapped[bool] = mapped_column(Boolean, default=False)
    is_demo: Mapped[bool] = mapped_column(Boolean, default=False, index=True)
    # 按字段记录来源，避免补充 HSP 时把既有 GSK 分数错误归到新来源。
    field_sources: Mapped[dict] = mapped_column(JSON, default=dict)


class HazardRules(TimestampMixin, Base):
    """CAS 可以尚未存在于溶剂库，故不依赖 SolventData 外键。

    svhc_candidate 只表示清单身份；exclude_from_recommendations 是显式策略，
    不是由 SVHC 身份自动推断出的普遍禁用结论。
    """

    __tablename__ = "hazard_rules"
    __table_args__ = (
        UniqueConstraint("cas", "rule_code", "source_id", name="uq_hazard_source_rule"),
        CheckConstraint(
            "rule_type IN ('svhc_candidate','authorization','restriction','advisory')",
            name="ck_rule_type",
        ),
        CheckConstraint("severity IN ('info','warning','danger')", name="ck_severity"),
        CheckConstraint(
            "effective_to IS NULL OR effective_from IS NULL OR effective_to >= effective_from",
            name="ck_rule_dates",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    cas: Mapped[str] = mapped_column(String(12), index=True)
    name: Mapped[str] = mapped_column(String(200))
    rule_code: Mapped[str] = mapped_column(String(100))
    rule_type: Mapped[str] = mapped_column(String(30))
    severity: Mapped[str] = mapped_column(String(20), default="warning")
    warning: Mapped[str] = mapped_column(Text)
    conditions: Mapped[str | None] = mapped_column(Text)
    is_svhc: Mapped[bool] = mapped_column(Boolean, default=False)
    exclude_from_recommendations: Mapped[bool] = mapped_column(Boolean, default=False)
    active: Mapped[bool] = mapped_column(Boolean, default=True)
    effective_from: Mapped[date | None] = mapped_column(Date)
    effective_to: Mapped[date | None] = mapped_column(Date)
    source_id: Mapped[str] = mapped_column(String(100), index=True)
    provenance: Mapped[dict] = mapped_column(JSON)
    is_demo: Mapped[bool] = mapped_column(Boolean, default=False)


class UserEvaluations(TimestampMixin, Base):
    """私有历史快照，不级联绑定公开数据，因此同步不会改写历史结果。"""

    __tablename__ = "user_evaluations"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    user_id: Mapped[str | None] = mapped_column(String(100), index=True)
    reaction: Mapped[str] = mapped_column(Text)
    amounts: Mapped[dict] = mapped_column(JSON)
    evaluation_result: Mapped[dict] = mapped_column(JSON)
    input_format: Mapped[str] = mapped_column(String(20), default="json")
    mass_unit: Mapped[str] = mapped_column(String(20), default="g")
    waste_boundary: Mapped[str] = mapped_column(Text)
    scoring_version: Mapped[str] = mapped_column(String(100))
    dataset_versions: Mapped[dict] = mapped_column(JSON, default=dict)


class DatasetSyncRuns(Base):
    """同步审计：成功记录与数据同事务，失败记录于回滚后独立提交。"""

    __tablename__ = "dataset_sync_runs"
    __table_args__ = (CheckConstraint("status IN ('success','failed')", name="ck_sync_status"),)

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    source_id: Mapped[str] = mapped_column(String(100), index=True)
    dataset_kind: Mapped[str] = mapped_column(String(20))
    source_version: Mapped[str] = mapped_column(String(100))
    source_location: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(20))
    sha256: Mapped[str | None] = mapped_column(String(64))
    started_at: Mapped[datetime] = mapped_column(UTCDateTime())
    finished_at: Mapped[datetime] = mapped_column(UTCDateTime(), default=utc_now)
    inserted: Mapped[int] = mapped_column(default=0)
    updated: Mapped[int] = mapped_column(default=0)
    unchanged: Mapped[int] = mapped_column(default=0)
    error: Mapped[str | None] = mapped_column(Text)
    provenance: Mapped[dict] = mapped_column(JSON)


class ManagedDataset(TimestampMixin, Base):
    """持久化数据源目录；用户数据在本机保存，与公开快照分开。"""

    __tablename__ = "managed_datasets"
    id: Mapped[str] = mapped_column(String(100), primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    scope: Mapped[str] = mapped_column(String(20))  # public / personal / local
    kind: Mapped[str] = mapped_column(String(20))
    adapter: Mapped[str] = mapped_column(String(50), default="upload")
    location: Mapped[str] = mapped_column(Text, default="")
    license: Mapped[str] = mapped_column(Text)
    attribution: Mapped[str] = mapped_column(Text, default="")
    region: Mapped[str] = mapped_column(String(200), default="")
    score_method: Mapped[str | None] = mapped_column(Text)
    column_map: Mapped[dict] = mapped_column(JSON, default=dict)
    format: Mapped[str] = mapped_column(String(10), default="json")
    enabled: Mapped[bool] = mapped_column(Boolean, default=True)
    priority: Mapped[int] = mapped_column(default=100)
    interval_hours: Mapped[int] = mapped_column(default=0)
    jitter_minutes: Mapped[int] = mapped_column(default=0)
    next_check_at: Mapped[datetime | None] = mapped_column(UTCDateTime())
    last_checked_at: Mapped[datetime | None] = mapped_column(UTCDateTime())
    last_success_at: Mapped[datetime | None] = mapped_column(UTCDateTime())
    status: Mapped[str] = mapped_column(String(30), default="never")
    error: Mapped[str | None] = mapped_column(Text)
    current_revision: Mapped[str | None] = mapped_column(String(36))
    consecutive_failures: Mapped[int] = mapped_column(default=0)


class DatasetRevision(Base):
    __tablename__ = "dataset_revisions"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    dataset_id: Mapped[str] = mapped_column(String(100), index=True)
    created_at: Mapped[datetime] = mapped_column(UTCDateTime(), default=utc_now)
    version: Mapped[str] = mapped_column(String(100))
    sha256: Mapped[str] = mapped_column(String(64))
    records: Mapped[list] = mapped_column(JSON)
    provenance: Mapped[dict] = mapped_column(JSON)
    notes: Mapped[list] = mapped_column(JSON, default=list)


class DatasetBaseline(Base):
    """首次接管前的旧数据快照，用于停用覆盖层后恢复；不包含用户评估历史。"""

    __tablename__ = "dataset_baseline"
    id: Mapped[int] = mapped_column(primary_key=True)
    solvents: Mapped[list] = mapped_column(JSON)
    hazards: Mapped[list] = mapped_column(JSON)


class DatasetLease(Base):
    """数据库级同步互斥，防止多进程同时应用快照。"""

    __tablename__ = "dataset_lease"
    id: Mapped[int] = mapped_column(primary_key=True)
    owner: Mapped[str | None] = mapped_column(String(36))
    expires_at: Mapped[datetime | None] = mapped_column(UTCDateTime())
