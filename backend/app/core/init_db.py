"""Apply Alembic migrations to the configured database.

Usage (from the ``backend`` folder):

    python -m app.core.init_db
"""

import os
from pathlib import Path

from alembic import command
from alembic.config import Config
from sqlalchemy.engine import make_url

from app.core.config import get_settings

# backend/app/core/init_db.py -> parents[2] is backend/
BACKEND_DIR = Path(__file__).resolve().parents[2]
ALEMBIC_INI = BACKEND_DIR / "alembic.ini"
MIGRATIONS_DIR = BACKEND_DIR / "migrations"


def _ensure_sqlite_folder(database_url: str) -> None:
    url = make_url(database_url)
    if url.get_backend_name() != "sqlite":
        return
    db_path = url.database
    if db_path and db_path != ":memory:":
        os.makedirs(os.path.dirname(os.path.abspath(db_path)), exist_ok=True)


def run_migrations() -> None:
    """Upgrade the database to the latest Alembic revision."""
    _ensure_sqlite_folder(get_settings().DATABASE_URL)

    cfg = Config(str(ALEMBIC_INI))
    cfg.set_main_option("script_location", str(MIGRATIONS_DIR))
    command.upgrade(cfg, "head")


if __name__ == "__main__":
    run_migrations()
    print("Database migrated.")
