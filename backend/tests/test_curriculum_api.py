"""Curriculum browsing API tests. The hierarchy is walked through the API only, with no hardcoded ids."""

import pytest
from sqlalchemy import select

from app.core.database import SessionLocal
from app.models import Board

BASE = "/api/curriculum"


def _auth(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _get_ok(client, token: str, path: str):
    resp = client.get(path, headers=_auth(token))
    assert resp.status_code == 200, f"{path}: {resp.text}"
    return resp.json()


def test_boards_requires_authentication(client):
    assert client.get(f"{BASE}/boards").status_code == 401


def test_boards_lists_ksb(client, demo_token):
    boards = _get_ok(client, demo_token, f"{BASE}/boards")
    codes = [board["code"] for board in boards]
    assert codes.count("KSB") == 1


def test_hierarchy_walk_and_relationships(client, demo_token):
    boards = _get_ok(client, demo_token, f"{BASE}/boards")
    board = boards[0]

    classes = _get_ok(client, demo_token, f"{BASE}/boards/{board['id']}/classes")
    class_8 = next(c for c in classes if c["level_number"] == 8)

    subjects = _get_ok(client, demo_token, f"{BASE}/classes/{class_8['id']}/subjects")
    science_matches = [s for s in subjects if s["code"] == "science"]
    assert len(science_matches) == 1
    subject = science_matches[0]
    assert subject["class_id"] == class_8["id"]

    chapters = _get_ok(client, demo_token, f"{BASE}/subjects/{subject['id']}/chapters")
    assert len(chapters) == 3
    numbers = [chapter["number"] for chapter in chapters]
    assert numbers == sorted(numbers)

    for chapter in chapters:
        assert chapter["subject_id"] == subject["id"]

        topics = _get_ok(client, demo_token, f"{BASE}/chapters/{chapter['id']}/topics")
        assert len(topics) >= 2

        for topic in topics:
            assert topic["chapter_id"] == chapter["id"]

            lessons = _get_ok(client, demo_token, f"{BASE}/topics/{topic['id']}/lessons")
            assert len(lessons) == 1
            lesson_summary = lessons[0]
            assert lesson_summary["topic_id"] == topic["id"]

            detail = _get_ok(client, demo_token, f"{BASE}/lessons/{lesson_summary['id']}")
            assert detail["topic_id"] == topic["id"]
            assert detail["body_kn"].strip()
            assert isinstance(detail["key_terms"], list)
            assert detail["is_sample"] is True
            assert "Not official Karnataka State Board text" in (detail["source_note"] or "")


@pytest.mark.parametrize(
    "path",
    [
        "/api/curriculum/boards/999999/classes",
        "/api/curriculum/classes/999999/subjects",
        "/api/curriculum/subjects/999999/chapters",
        "/api/curriculum/chapters/999999/topics",
        "/api/curriculum/topics/999999/lessons",
        "/api/curriculum/lessons/999999",
    ],
)
def test_unknown_ids_return_404(client, demo_token, path):
    resp = client.get(path, headers=_auth(demo_token))
    assert resp.status_code == 404


@pytest.mark.parametrize("path", ["/api/curriculum/lessons/abc", "/api/curriculum/lessons/0"])
def test_invalid_ids_return_422(client, demo_token, path):
    resp = client.get(path, headers=_auth(demo_token))
    assert resp.status_code == 422


def test_inactive_board_is_hidden_and_its_classes_return_404(client, demo_token):
    db = SessionLocal()
    try:
        board = db.scalar(select(Board).where(Board.code == "KSB"))
        assert board is not None
        board_id = board.id
        board.is_active = False
        db.commit()

        listed = _get_ok(client, demo_token, f"{BASE}/boards")
        assert board_id not in [item["id"] for item in listed]

        resp = client.get(f"{BASE}/boards/{board_id}/classes", headers=_auth(demo_token))
        assert resp.status_code == 404
    finally:
        board.is_active = True
        db.commit()
        db.close()
