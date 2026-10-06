"""显式配置；默认仅用于本机，不自动下载数据或启动同步任务。"""

import os
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field, SecretStr


class Settings(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    database_url: str | None = None
    sources_config: Path | None = None
    sync_api_key: SecretStr | None = None
    allow_demo: bool = False
    max_body_bytes: int = Field(default=3 * 1024 * 1024, gt=0)
    max_upload_bytes: int = Field(default=2 * 1024 * 1024, gt=0)
    max_csv_rows: int = Field(default=200, gt=0, le=10000)
    cors_origins: list[str] = Field(default_factory=list)
    frontend_dir: Path = Path(__file__).resolve().parents[1] / "frontend" / "dist"
    pdf_font_path: Path | None = None
    auto_update: bool = False

    @classmethod
    def from_env(cls):
        demo = os.getenv("OQW_ALLOW_DEMO", "false").lower()
        if demo not in ("true", "false"):
            raise ValueError("OQW_ALLOW_DEMO 只接受 true/false")
        return cls(
            database_url=os.getenv("OQW_DATABASE_URL") or None,
            sources_config=os.getenv("OQW_SOURCES_CONFIG") or None,
            sync_api_key=os.getenv("OQW_SYNC_API_KEY") or None,
            allow_demo=demo == "true",
            pdf_font_path=os.getenv("OQW_PDF_FONT") or None,
            auto_update=os.getenv("OQW_AUTO_UPDATE", "false").lower() == "true",
            cors_origins=[
                origin.strip()
                for origin in os.getenv("OQW_CORS_ORIGINS", "").split(",")
                if origin.strip()
            ],
        )
