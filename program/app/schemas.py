"""Pydantic v2 API 契约：禁用未知字段，不将字符串/布尔值当质量。"""

from datetime import date
from typing import Annotated, Any, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from chem_engine.hsp_matcher import _cas

Positive = Annotated[float, Field(strict=True, gt=0, le=1e12, allow_inf_nan=False)]
NonNegative = Annotated[float, Field(strict=True, ge=0, le=1e12, allow_inf_nan=False)]
Score = Annotated[float, Field(strict=True, ge=0, le=100, allow_inf_nan=False)]
Text = Annotated[str, Field(min_length=1, max_length=4096)]


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True, str_strip_whitespace=True)


class Reactant(StrictModel):
    smiles: Text
    mass: Positive
    coefficient: Positive = 1.0


class Product(Reactant):
    pass


class SolventReference(StrictModel):
    cas: Annotated[str, Field(max_length=12)] | None = None
    name: Annotated[str, Field(min_length=1, max_length=200)] | None = None

    @field_validator("cas")
    @classmethod
    def valid_cas(cls, value):
        return _cas(value) if value is not None else None

    @model_validator(mode="after")
    def require_identifier(self):
        if self.cas is None and self.name is None:
            raise ValueError("至少提供 CAS 或名称")
        return self


class SolventInput(SolventReference):
    mass: Positive | None = None


class ExternalAssessment(StrictModel):
    score: Score
    basis: Text


class EvaluationRequest(StrictModel):
    reactants: Annotated[list[Reactant], Field(min_length=1, max_length=50)]
    product: Product
    solvents: Annotated[list[SolventInput], Field(max_length=30)] = Field(default_factory=list)
    mass_unit: Literal["g", "kg", "mg"] = "g"
    total_waste_mass: NonNegative | None = None
    waste_boundary: Text | None = None
    energy_assessment: ExternalAssessment | None = None
    process_safety_assessment: ExternalAssessment | None = None
    persist: bool = True

    @model_validator(mode="after")
    def require_waste_boundary(self):
        if (
            sum(len(item.smiles) + 1 for item in self.reactants) + len(self.product.smiles) + 2
            > 10000
        ):
            raise ValueError("完整反应 SMILES 长度不能超过 10000 字符")
        if self.total_waste_mass is not None and self.waste_boundary is None:
            raise ValueError("提供废弃物质量时必须说明 waste_boundary（是否含水/回收物流等）")
        return self


class DisposalQuote(StrictModel):
    cas: str
    cost_per_kg: NonNegative
    source: Text

    @field_validator("cas")
    @classmethod
    def valid_cas(cls, value):
        return _cas(value)


class CostContext(StrictModel):
    waste_mass_kg: Positive
    currency: Annotated[str, Field(pattern=r"^[A-Z]{3}$")]
    region: Annotated[str, Field(min_length=1, max_length=200)]
    quote_date: Annotated[str, Field(pattern=r"^\d{4}-\d{2}-\d{2}$")]
    quotes: Annotated[list[DisposalQuote], Field(min_length=1, max_length=100)]

    @field_validator("quote_date")
    @classmethod
    def valid_date(cls, value):
        date.fromisoformat(value)
        return value

    @model_validator(mode="after")
    def unique_quotes(self):
        if len({quote.cas for quote in self.quotes}) != len(self.quotes):
            raise ValueError("每个 CAS 只允许一条同口径报价")
        return self


class SwapRequest(SolventReference):
    top_k: Annotated[int, Field(ge=1, le=10)] = 3
    cost_context: CostContext | None = None


class SyncRequest(StrictModel):
    source_ids: Annotated[list[str], Field(min_length=1, max_length=50)] | None = None

    @field_validator("source_ids")
    @classmethod
    def unique_sources(cls, value):
        if value is not None and (
            len(set(value)) != len(value) or any(not item.strip() for item in value)
        ):
            raise ValueError("source_ids 不可重复或为空")
        return value


class MetricsResponse(StrictModel):
    atom_economy: float
    e_factor: float | None
    rme: float


class EvaluationResponse(StrictModel):
    evaluation_id: str | None
    evaluated_at: str
    metrics: MetricsResponse
    score: dict[str, Any]
    radar: dict[str, Any]
    solvent_warnings: list[dict[str, Any]]
    solvents: list[dict[str, Any]]
    data_notes: list[str]
    dataset_versions: dict[str, Any]
    mass_basis: dict[str, Any]
    demo_only: bool


class SwapResponse(StrictModel):
    status: Literal["ok", "no_candidates"]
    target: dict[str, Any]
    replacements: list[dict[str, Any]]
    skipped: list[dict[str, Any]]
    notes: list[str]
    demo_only: bool


class ImportResponse(StrictModel):
    total_rows: int
    successful_rows: int
    failed_rows: int
    persisted_rows: int
    rows: list[dict[str, Any]]


class SyncResponse(StrictModel):
    status: Literal["success", "partial", "failed"]
    results: list[dict[str, Any]]


class ErrorBody(StrictModel):
    code: str
    message: str
    details: Any = None


class ErrorResponse(StrictModel):
    error: ErrorBody


class ReportRequest(StrictModel):
    evaluation_id: Annotated[str, Field(pattern=r"^[0-9a-fA-F-]{36}$")] | None = None
    evaluation: EvaluationRequest | None = None

    @model_validator(mode="after")
    def one_source(self):
        if (self.evaluation_id is None) == (self.evaluation is None):
            raise ValueError("只提供 evaluation_id 或 evaluation 中的一项")
        if self.evaluation_id is not None:
            from uuid import UUID

            UUID(self.evaluation_id)
        return self
