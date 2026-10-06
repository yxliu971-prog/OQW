"""独立于网页的更新入口，可由 Windows 任务计划程序调用。"""

import argparse
import json
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import Session

from . import create_db_engine, initialize_database
from .data_manager import register_catalog, sync_one
from .dataset_loader import DatasetLoadError
from .models import ManagedDataset, utc_now


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--database-url")
    parser.add_argument("--source", action="append")
    parser.add_argument("--due", action="store_true", help="仅更新已启用且到期的来源")
    parser.add_argument("--log", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    engine = create_db_engine(args.database_url or f"sqlite:///{root / 'data' / 'oqw.sqlite3'}")
    initialize_database(engine)
    register_catalog(engine)
    output = []
    try:
        with Session(engine) as session:
            query = select(ManagedDataset.id).where(
                ManagedDataset.enabled.is_(True), ManagedDataset.adapter != "upload"
            )
            if args.due:
                query = query.where(
                    ManagedDataset.interval_hours > 0, ManagedDataset.next_check_at <= utc_now()
                )
            identifiers = args.source or list(
                session.scalars(query.order_by(ManagedDataset.priority))
            )
        for identifier in identifiers:
            try:
                output.append(
                    {"id": identifier, **sync_one(engine, identifier, only_if_due=args.due)}
                )
            except DatasetLoadError as exc:
                output.append({"id": identifier, "status": "failed", "error": str(exc)})
    finally:
        engine.dispose()
    result = json.dumps(
        {"checked_at": utc_now().isoformat(), "results": output}, ensure_ascii=False
    )
    if args.log:
        args.log.parent.mkdir(parents=True, exist_ok=True)
        with args.log.open("a", encoding="utf-8") as file:
            file.write(result + "\n")
    print(result)
    return 1 if any(item["status"] == "failed" for item in output) else 0


if __name__ == "__main__":
    raise SystemExit(main())
