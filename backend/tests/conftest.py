"""Shared pytest fixtures.

The environment is configured BEFORE any ``app`` module is imported, so every engine, session and
migration in this test run points at ``backend/data/test_wondernest.db`` and never at
``backend/data/wondernest.db``.
"""

import os
from collections.abc import Iterator
from pathlib import Path

TEST_DB = Path(__file__).resolve().parents[1] / "data" / "test_wondernest.db"
if TEST_DB.exists():
    TEST_DB.unlink()
os.environ["DATABASE_URL"] = f"sqlite:///{TEST_DB.as_posix()}"
os.environ["DEMO_PASSWORD"] = "Demo@12345"

from app.core.config import get_settings  # noqa: E402

get_settings.cache_clear()

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402
from sqlalchemy import delete  # noqa: E402

from app.core.database import SessionLocal, engine  # noqa: E402
from app.core.init_db import run_migrations  # noqa: E402
from app.curriculum.seed import seed_curriculum  # noqa: E402
from app.main import app  # noqa: E402
from app.models import User  # noqa: E402
from app.security.passwords import hash_password  # noqa: E402

DEMO_PASSWORD = "Demo@12345"
ISO_PASSWORD = "Iso@12345"


@pytest.fixture(scope="session", autouse=True)
def migrated_db() -> Iterator[None]:
    """Migrate the test database to head and load the sample curriculum once per session."""
    run_migrations()
    db = SessionLocal()
    try:
        seed_curriculum(db, DEMO_PASSWORD)
    finally:
        db.close()
    yield
    engine.dispose()


@pytest.fixture(scope="session")
def client(migrated_db) -> Iterator[TestClient]:
    with TestClient(app) as c:
        yield c


@pytest.fixture
def login_token(client):
    """Factory: log in with username and password and return the access token."""

    def _login(username: str, password: str) -> str:
        resp = client.post("/api/auth/login", json={"username": username, "password": password})
        assert resp.status_code == 200, resp.text
        return resp.json()["access_token"]

    return _login


@pytest.fixture
def demo_token(login_token) -> str:
    return login_token("demo_student", DEMO_PASSWORD)


@pytest.fixture(scope="session")
def isolation_users(migrated_db) -> Iterator[dict[str, int]]:
    """Create dedicated student and teacher accounts for isolation tests. Returns username -> id."""
    specs = [
        {"username": "iso_student_a", "role": "student", "preferred_language": "kn", "display_name": "Test A"},
        {"username": "iso_student_b", "role": "student", "preferred_language": "kn", "display_name": "Test B"},
        {"username": "iso_teacher", "role": "teacher", "preferred_language": "kn", "display_name": "Test Teacher"},
    ]
    db = SessionLocal()
    try:
        users = [
            User(password_hash=hash_password(ISO_PASSWORD), **spec)
            for spec in specs
        ]
        db.add_all(users)
        db.commit()
        ids = {user.username: user.id for user in users}
    finally:
        db.close()

    yield ids

    db = SessionLocal()
    try:
        db.execute(delete(User).where(User.id.in_(list(ids.values()))))
        db.commit()
    finally:
        db.close()


@pytest.fixture
def token_for(client, isolation_users):
    """Factory: log in an isolation user with the isolation password and return the access token."""

    def _token(username: str) -> str:
        resp = client.post("/api/auth/login", json={"username": username, "password": ISO_PASSWORD})
        assert resp.status_code == 200, resp.text
        return resp.json()["access_token"]

    return _token
