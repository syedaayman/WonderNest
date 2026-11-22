"""Learning objectives persistence and API tests. Lesson ids are discovered through the API, never hardcoded."""

import sqlite3
from pathlib import Path

from app.core.database import SessionLocal
from app.curriculum.seed import seed_curriculum

BASE = "/api/curriculum"
TEST_DB = Path(__file__).resolve().parents[1] / "data" / "test_wondernest.db"
DEMO_PASSWORD = "Demo@12345"
EXPECTED_OBJECTIVES = 54
EXPECTED_TOPICS = 27
OBJECTIVES_PER_LESSON = 2


def _auth(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _get_ok(client, token: str, path: str):
    resp = client.get(path, headers=_auth(token))
    assert resp.status_code == 200, f"{path}: {resp.text}"
    return resp.json()


def _connect() -> sqlite3.Connection:
    return sqlite3.connect(TEST_DB)


def _walk_topics(client, token: str) -> list[dict]:
    """Return every topic of Class 8 Science, reached through the API hierarchy."""
    boards = _get_ok(client, token, f"{BASE}/boards")
    classes = _get_ok(client, token, f"{BASE}/boards/{boards[0]['id']}/classes")
    class_8 = next(c for c in classes if c["level_number"] == 8)
    subjects = _get_ok(client, token, f"{BASE}/classes/{class_8['id']}/subjects")
    subject = next(s for s in subjects if s["code"] == "science")
    chapters = _get_ok(client, token, f"{BASE}/subjects/{subject['id']}/chapters")
    topics: list[dict] = []
    for chapter in chapters:
        topics.extend(_get_ok(client, token, f"{BASE}/chapters/{chapter['id']}/topics"))
    return topics


def _walk_lessons(client, token: str) -> list[dict]:
    """Return the lesson summary for every topic reached by the hierarchy walk."""
    lessons: list[dict] = []
    for topic in _walk_topics(client, token):
        lessons.extend(_get_ok(client, token, f"{BASE}/topics/{topic['id']}/lessons"))
    return lessons


def test_objectives_persisted_in_database():
    conn = _connect()
    try:
        total = conn.execute("SELECT COUNT(*) FROM learning_objectives").fetchone()[0]
        orphans = conn.execute(
            "SELECT COUNT(*) FROM learning_objectives "
            "WHERE topic_id NOT IN (SELECT id FROM topics)"
        ).fetchone()[0]
        distinct_topics = conn.execute(
            "SELECT COUNT(DISTINCT topic_id) FROM learning_objectives"
        ).fetchone()[0]
    finally:
        conn.close()

    assert total == EXPECTED_OBJECTIVES
    assert orphans == 0
    assert distinct_topics == EXPECTED_TOPICS


def test_objective_relationship_to_lesson(client, demo_token):
    topics = _walk_topics(client, demo_token)
    assert topics, "hierarchy walk returned no topics"
    first_lessons = _get_ok(client, demo_token, f"{BASE}/topics/{topics[0]['id']}/lessons")
    assert len(first_lessons) == 1
    lesson_id = first_lessons[0]["id"]

    resp = client.get(f"{BASE}/lessons/{lesson_id}/objectives", headers=_auth(demo_token))
    assert resp.status_code == 200, resp.text
    items = resp.json()
    assert len(items) == OBJECTIVES_PER_LESSON
    for item in items:
        assert item["lesson_id"] == lesson_id


def test_objectives_ordered_by_position(client, demo_token):
    lessons = _walk_lessons(client, demo_token)
    assert len(lessons) == EXPECTED_TOPICS
    for lesson in lessons:
        items = _get_ok(client, demo_token, f"{BASE}/lessons/{lesson['id']}/objectives")
        assert [item["position"] for item in items] == [1, 2], f"lesson {lesson['id']}"


def test_kannada_unicode_preserved(client, demo_token):
    lessons = _walk_lessons(client, demo_token)
    assert lessons, "hierarchy walk returned no lessons"
    items = _get_ok(client, demo_token, f"{BASE}/lessons/{lessons[0]['id']}/objectives")
    assert items, "first lesson has no objectives"
    for item in items:
        text = item["text_kn"]
        assert isinstance(text, str)
        assert text.strip()
        assert text != "?"
        assert "\ufffd" not in text
        assert any(0x0C80 <= ord(ch) <= 0x0CFF for ch in text), text


def test_objectives_nonexistent_lesson_404(client, demo_token):
    resp = client.get(f"{BASE}/lessons/999999/objectives", headers=_auth(demo_token))
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Lesson not found."


def test_objectives_invalid_id(client, demo_token):
    # lesson_id is declared with Path(ge=1), so 0 and non-integers fail validation with 422.
    assert client.get(f"{BASE}/lessons/0/objectives", headers=_auth(demo_token)).status_code == 422
    assert client.get(f"{BASE}/lessons/abc/objectives", headers=_auth(demo_token)).status_code == 422


def test_objectives_requires_auth(client, demo_token):
    lessons = _walk_lessons(client, demo_token)
    assert lessons, "hierarchy walk returned no lessons"
    lesson_id = lessons[0]["id"]
    # get_current_user is a dependency that runs before the handler body, so a missing token
    # yields 401 for a real lesson id before any lookup happens.
    resp = client.get(f"{BASE}/lessons/{lesson_id}/objectives")
    assert resp.status_code == 401


def test_seed_objectives_idempotent():
    results: list[dict[str, int]] = []
    for _ in range(2):
        db = SessionLocal()
        try:
            results.append(seed_curriculum(db, DEMO_PASSWORD))
        finally:
            db.close()

    for result in results:
        assert result["learning_objectives"] == EXPECTED_OBJECTIVES

    conn = _connect()
    try:
        total = conn.execute("SELECT COUNT(*) FROM learning_objectives").fetchone()[0]
    finally:
        conn.close()
    assert total == EXPECTED_OBJECTIVES
