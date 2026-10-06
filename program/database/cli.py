"""命令行入口：python -m database init / sync / status。"""

import argparse
import json
import sys

from sqlalchemy import func, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from .dataset_loader import load_source_config
from .models import DatasetSyncRuns, HazardRules, SolventData, UserEvaluations
from .scheduler import iter_sync_cycles, sync_sources
from .session import create_db_engine, initialize_database


def _print(value):
    print(json.dumps(value, ensure_ascii=False, allow_nan=False, indent=2), flush=True)


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="OQW Phase 2 数据库与数据同步工具")
    parser.add_argument(
        "--database-url", help="SQLAlchemy URL；默认 OQW_DATABASE_URL 或 ./data/oqw.sqlite3"
    )
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("init", help="幂等建表，不加载数据")
    commands.add_parser("status", help="查看数据数量和最近 10 次同步，不显示私有反应内容")
    sync = commands.add_parser("sync", help="按配置同步 CSV/JSON 数据源")
    sync.add_argument("--config", required=True)
    sync.add_argument("--allow-demo", action="store_true", help="允许显式标记的合成演示数据")
    sync.add_argument("--watch", action="store_true", help="前台定期同步，Ctrl+C 停止")
    sync.add_argument(
        "--interval", type=float, default=86400, help="每轮完成后的间隔秒数，至少 60 秒"
    )
    args = parser.parse_args(argv)
    engine = None
    try:
        # 先校验配置再创建数据库文件。
        sources = load_source_config(args.config) if args.command == "sync" else None
        engine = create_db_engine(args.database_url)
        initialize_database(engine)
        if args.command == "init":
            _print(
                {
                    "status": "initialized",
                    "tables": [
                        "solvent_data",
                        "hazard_rules",
                        "user_evaluations",
                        "dataset_sync_runs",
                    ],
                }
            )
        elif args.command == "status":
            with Session(engine) as session:
                counts = {
                    model.__tablename__: session.scalar(select(func.count()).select_from(model))
                    for model in (SolventData, HazardRules, UserEvaluations, DatasetSyncRuns)
                }
                runs = session.scalars(
                    select(DatasetSyncRuns).order_by(DatasetSyncRuns.started_at.desc()).limit(10)
                )
                _print(
                    {
                        "counts": counts,
                        "recent_syncs": [
                            {
                                "run_id": run.id,
                                "source_id": run.source_id,
                                "version": run.source_version,
                                "status": run.status,
                                "inserted": run.inserted,
                                "updated": run.updated,
                                "unchanged": run.unchanged,
                                "error": run.error,
                                "finished_at": run.finished_at.isoformat(),
                            }
                            for run in runs
                        ],
                    }
                )
        elif args.watch:
            for result in iter_sync_cycles(
                engine, sources, interval_seconds=args.interval, allow_demo=args.allow_demo
            ):
                _print({"results": result})
        else:
            result = sync_sources(engine, sources, allow_demo=args.allow_demo)
            _print({"results": result})
            return 1 if any(item["status"] == "failed" for item in result) else 0
        return 0
    except KeyboardInterrupt:
        _print({"status": "stopped"})
        return 130
    except (ValueError, TypeError, OSError, SQLAlchemyError) as exc:
        error = type(exc).__name__ if isinstance(exc, SQLAlchemyError) else str(exc)
        print(json.dumps({"status": "failed", "error": error}, ensure_ascii=False), file=sys.stderr)
        return 1
    finally:
        if engine is not None:
            engine.dispose()
