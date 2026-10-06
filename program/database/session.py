"""显式初始化连接和表；导入本模块不会创建文件或连接数据库。"""

import json
import os
from pathlib import Path

from sqlalchemy import Engine, create_engine, event
from sqlalchemy.engine import URL, make_url
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from .models import Base


def create_db_engine(database_url: str | URL | None = None) -> Engine:
    """默认当前工作目录 data/oqw.sqlite3，也可指定 OQW_DATABASE_URL。"""
    value = database_url or os.getenv("OQW_DATABASE_URL")
    url = (
        make_url(value)
        if value
        else URL.create("sqlite+pysqlite", database=str(Path.cwd() / "data" / "oqw.sqlite3"))
    )
    options = {
        "json_serializer": lambda obj: json.dumps(obj, ensure_ascii=False, allow_nan=False),
        "pool_pre_ping": True,
    }
    if url.get_backend_name() == "sqlite":
        if url.database not in (None, "", ":memory:"):
            Path(url.database).expanduser().resolve().parent.mkdir(parents=True, exist_ok=True)
        else:
            options["poolclass"] = StaticPool
        options["connect_args"] = {"check_same_thread": False, "timeout": 10}
    engine = create_engine(url, **options)
    if url.get_backend_name() == "sqlite":

        @event.listens_for(engine, "connect")
        def configure_sqlite(connection, _):
            # SQLAlchemy 自己发出 BEGIN，修复 sqlite3 legacy transaction 模式。
            connection.isolation_level = None
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.execute("PRAGMA busy_timeout=10000")
            cursor.close()

        @event.listens_for(engine, "begin")
        def explicit_begin(connection):
            connection.exec_driver_sql("BEGIN")

    return engine


def initialize_database(engine: Engine) -> None:
    """幂等建表；不会删除数据，也不替代未来的 schema migration。"""
    Base.metadata.create_all(engine)


def session_factory(engine: Engine) -> sessionmaker:
    return sessionmaker(engine, expire_on_commit=False)
