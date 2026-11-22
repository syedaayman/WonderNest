"""Database-level checks against the isolated test database."""

import sqlite3
from pathlib import Path

from alembic.config import Config as AlembicConfig
from alembic.script import ScriptDirectory

import app.models  # noqa: F401  (registers every table on Base.metadata)
from app.core.database import Base, SessionLocal
from app.curriculum.seed import seed_curriculum

TEST_DB = Path(__file__).resolve().parents[1] / "data" / "test_wondernest.db"
DEMO_PASSWORD = "Demo@12345"
BACKEND_DIR = Path(__file__).resolve().parents[1]
_alembic_cfg = AlembicConfig(str(BACKEND_DIR / "alembic.ini"))
_alembic_cfg.set_main_option("script_location", str(BACKEND_DIR / "migrations"))
EXPECTED_HEAD = ScriptDirectory.from_config(_alembic_cfg).get_current_head()
COUNTED_TABLES = [
    "boards",
    "classes",
    "subjects",
    "chapters",
    "topics",
    "lessons",
    "practice_questions",
    "users",
    "learner_profiles",
]


def _connect() -> sqlite3.Connection:
    return sqlite3.connect(TEST_DB)


def _snapshot_counts() -> dict[str, int]:
    conn = _connect()
    try:
        return {
            table: conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            for table in COUNTED_TABLES
        }
    finally:
        conn.close()


def test_migration_head_is_applied():
    conn = _connect()
    try:
        rows = conn.execute("SELECT version_num FROM alembic_version").fetchall()
    finally:
        conn.close()
    assert [row[0] for row in rows] == [EXPECTED_HEAD]


def test_all_model_tables_exist():
    conn = _connect()
    try:
        existing = {
            row[0] for row in conn.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
        }
    finally:
        conn.close()
    for table_name in Base.metadata.tables:
        assert table_name in existing, f"missing table: {table_name}"


def test_seed_is_idempotent():
    before = _snapshot_counts()

    assert before["boards"] == 1
    assert before["classes"] == 1
    assert before["subjects"] == 1
    assert before["chapters"] == 10
    assert before["topics"] == 32
    assert before["lessons"] == 32
    assert before["practice_questions"] == 51

    db = SessionLocal()
    try:
        seed_curriculum(db, DEMO_PASSWORD)
    finally:
        db.close()

    after = _snapshot_counts()
    assert after == before

    conn = _connect()
    try:
        demo_rows = conn.execute(
            "SELECT COUNT(*) FROM users WHERE username = 'demo_student'"
        ).fetchone()[0]
    finally:
        conn.close()
    assert demo_rows == 1


def test_foreign_keys_clean():
    conn = _connect()
    try:
        violations = conn.execute("PRAGMA foreign_key_check").fetchall()
    finally:
        conn.close()
    assert violations == []
