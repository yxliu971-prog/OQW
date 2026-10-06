"""启动：python -m uvicorn app.main:app --host 127.0.0.1 --port 8000。"""

from contextlib import asynccontextmanager
from threading import Event, Lock, Thread

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import Engine, text

from database import create_db_engine, initialize_database
from database.data_manager import register_catalog, run_due
from database.dataset_loader import load_source_config

from .config import Settings
from .errors import install_handlers
from .middleware import BodyLimitMiddleware
from .routes import data_library, datasets, evaluation, reports, swaps
from .schemas import ErrorResponse


def create_app(settings: Settings | None = None, *, engine: Engine | None = None) -> FastAPI:
    configuration = settings if settings is not None else Settings.from_env()

    @asynccontextmanager
    async def lifespan(application: FastAPI):
        owned = engine is None
        active_engine = (
            engine if engine is not None else create_db_engine(configuration.database_url)
        )
        try:
            initialize_database(active_engine)
            register_catalog(active_engine)
            sources = (
                load_source_config(configuration.sources_config)
                if configuration.sources_config
                else []
            )
            application.state.engine = active_engine
            application.state.sources = {source.source_id: source for source in sources}
            application.state.sync_lock = Lock()
            stop = Event()
            worker = None
            if configuration.auto_update and not configuration.allow_demo:
                worker = Thread(
                    target=run_due,
                    args=(active_engine, stop),
                    daemon=True,
                    name="oqw-dataset-updater",
                )
                worker.start()
            yield
        finally:
            if "stop" in locals():
                stop.set()
            if "worker" in locals() and worker:
                worker.join(timeout=2)
            if owned:
                active_engine.dispose()

    application = FastAPI(
        title="OQW 绿色智能化学解决方案系统",
        version="0.5.0",
        description="确定性绿色化学指标、HSP 替换、私有配方 CSV 诊断与受控数据同步。",
        lifespan=lifespan,
    )
    application.state.settings = configuration
    install_handlers(application)
    application.add_middleware(BodyLimitMiddleware, max_bytes=configuration.max_body_bytes)
    if configuration.cors_origins:
        application.add_middleware(
            CORSMiddleware,
            allow_origins=configuration.cors_origins,
            allow_methods=["GET", "POST"],
            allow_headers=["Content-Type", "X-OQW-Admin-Key"],
        )
    errors = {code: {"model": ErrorResponse} for code in (400, 401, 404, 409, 413, 415, 422, 503)}
    application.include_router(evaluation.router, prefix="/api/v1", responses=errors)
    application.include_router(swaps.router, prefix="/api/v1", responses=errors)
    application.include_router(datasets.router, prefix="/api/v1", responses=errors)
    application.include_router(reports.router, prefix="/api/v1", responses=errors)
    application.include_router(data_library.router, prefix="/api/v1", responses=errors)

    @application.get("/health", tags=["服务状态"], summary="检查服务与数据库连接")
    def health(request: Request):
        with request.app.state.engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"status": "ok", "version": "0.5.0", "demo_enabled": configuration.allow_demo}

    # 固定资源路径，避免 SPA 回退吞掉 API 404 或暴露源码目录。
    assets = configuration.frontend_dir / "assets"
    if assets.is_dir():
        application.mount("/assets", StaticFiles(directory=assets), name="frontend-assets")

    @application.get("/", include_in_schema=False)
    def frontend():
        index = configuration.frontend_dir / "index.html"
        if not index.is_file():
            from .errors import APIError

            raise APIError(503, "frontend_not_built", "前端尚未构建，请在 frontend 执行 pnpm build")
        return FileResponse(index, headers={"Cache-Control": "no-cache"})

    return application


app = create_app()
