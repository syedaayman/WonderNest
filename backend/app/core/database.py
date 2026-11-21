"""SQLAlchemy engine, session factory, declarative base and request-scoped session dependency.

The database is selected purely through ``Settings.DATABASE_URL``; no dialect-specific
SQL lives here, so switching to PostgreSQL only requires changing the URL.
"""

import os
from collections.abc import Generator

from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine, make_url
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.core.config import get_settings


class Base(DeclarativeBase):
    pass


def _build_engine(database_url: str) -> Engine:
    url = make_url(database_url)

    if url.get_backend_name() == "sqlite":
        connect_args = {"check_same_thread": False}
        db_path = url.database
        if db_path and db_path != ":memory:":
            parent = os.path.dirname(os.path.abspath(db_path))
            os.makedirs(parent, exist_ok=True)
        eng = create_engine(database_url, connect_args=connect_args, future=True)

        @event.listens_for(eng, "connect")
        def _enable_sqlite_foreign_keys(dbapi_connection, _connection_record) -> None:
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.close()

        return eng

    return create_engine(database_url, future=True)


engine: Engine = _build_engine(get_settings().DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
