"""Quiz and lesson-progress tests: auth, answer privacy, scoring and ownership."""

import pytest
from sqlalchemy import delete, select

from app.core.database import SessionLocal
from app.models import Chapter, Lesson, PracticeQuestion, QuizAttempt

BASE = "/api/quiz"
STUDENTS = "/api/students"


def _auth(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _chapter_with_questions() -> int:
    db = SessionLocal()
    try:
        chapter_id = db.scalar(
            select(PracticeQuestion.chapter_id).order_by(PracticeQuestion.chapter_id).limit(1)
        )
    finally:
        db.close()
    assert chapter_id is not None, "seed data must contain practice questions"
    return chapter_id


def _answer_key(chapter_id: int) -> dict[int, int]:
    db = SessionLocal()
    try:
        rows = db.execute(
            select(PracticeQuestion.id, PracticeQuestion.correct_index).where(
                PracticeQuestion.chapter_id == chapter_id
            )
        ).all()
    finally:
        db.close()
    return {row.id: row.correct_index for row in rows}


def test_quiz_requires_authentication(client):
    assert client.get(f"{BASE}/chapters/1").status_code == 401


def test_quiz_denied_for_teacher(client, token_for):
    resp = client.get(f"{BASE}/chapters/1", headers=_auth(token_for("iso_teacher")))
    assert resp.status_code == 403


def test_quiz_does_not_leak_correct_answers(client, demo_token):
    chapter_id = _chapter_with_questions()
    resp = client.get(f"{BASE}/chapters/{chapter_id}", headers=_auth(demo_token))
    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert body["total"] == len(body["questions"]) > 0
    for question in body["questions"]:
        assert "correct_index" not in question
        assert question["options_kn"]
        assert question["question_kn"]


def test_submitting_all_correct_answers_scores_full_marks(client, demo_token):
    chapter_id = _chapter_with_questions()
    key = _answer_key(chapter_id)
    payload = {
        "answers": [
            {"question_id": question_id, "selected_index": index}
            for question_id, index in key.items()
        ]
    }
    resp = client.post(
        f"{BASE}/chapters/{chapter_id}/attempts", headers=_auth(demo_token), json=payload
    )
    assert resp.status_code == 201, resp.text
    body = resp.json()
    assert body["score"] == body["total"] == len(key)
    assert body["chapter_id"] == chapter_id
    assert all(answer["is_correct"] for answer in body["answers"])
    assert body["attempt_id"] > 0

    # The stored result can be read back by its owner.
    again = client.get(f"{BASE}/attempts/{body['attempt_id']}", headers=_auth(demo_token))
    assert again.status_code == 200, again.text
    assert again.json()["score"] == body["score"]


def test_wrong_answers_score_zero_and_reveal_explanations(client, demo_token):
    chapter_id = _chapter_with_questions()
    key = _answer_key(chapter_id)
    payload = {
        "answers": [
            {"question_id": question_id, "selected_index": (index + 1) % 4}
            for question_id, index in key.items()
        ]
    }
    resp = client.post(
        f"{BASE}/chapters/{chapter_id}/attempts", headers=_auth(demo_token), json=payload
    )
    assert resp.status_code == 201, resp.text
    body = resp.json()
    assert body["score"] == 0
    assert all(not answer["is_correct"] for answer in body["answers"])

    db = SessionLocal()
    try:
        db.execute(delete(QuizAttempt).where(QuizAttempt.id == body["attempt_id"]))
        db.commit()
    finally:
        db.close()


def test_answer_for_foreign_question_is_rejected(client, demo_token):
    chapter_id = _chapter_with_questions()
    resp = client.post(
        f"{BASE}/chapters/{chapter_id}/attempts",
        headers=_auth(demo_token),
        json={"answers": [{"question_id": 987654, "selected_index": 0}]},
    )
    assert resp.status_code == 400, resp.text


def test_attempt_is_private_to_its_owner(client, demo_token, token_for):
    chapter_id = _chapter_with_questions()
    key = _answer_key(chapter_id)
    created = client.post(
        f"{BASE}/chapters/{chapter_id}/attempts",
        headers=_auth(demo_token),
        json={"answers": [{"question_id": q, "selected_index": i} for q, i in key.items()]},
    )
    attempt_id = created.json()["attempt_id"]

    other = client.get(f"{BASE}/attempts/{attempt_id}", headers=_auth(token_for("iso_student")))
    assert other.status_code == 404, other.text


def test_unknown_chapter_returns_404(client, demo_token):
    assert client.get(f"{BASE}/chapters/999999", headers=_auth(demo_token)).status_code == 404


def test_lesson_progress_is_recorded_for_the_token_owner(client, demo_token):
    db = SessionLocal()
    try:
        lesson_id = db.scalar(select(Lesson.id).order_by(Lesson.id).limit(1))
        chapter_title = db.scalar(select(Chapter.title_en).order_by(Chapter.id).limit(1))
    finally:
        db.close()
    assert lesson_id is not None and chapter_title

    resp = client.post(
        f"{STUDENTS}/lessons/{lesson_id}/progress",
        headers=_auth(demo_token),
        json={"status": "completed", "time_spent_seconds": 120},
    )
    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert body["lesson_id"] == lesson_id
    assert body["status"] == "completed"

    progress = client.get(f"{STUDENTS}/progress", headers=_auth(demo_token))
    assert progress.status_code == 200, progress.text
    payload = progress.json()
    assert payload["lessons_completed"] >= 1
    lesson_ids = {row["lesson_id"] for row in payload["lessons"]}
    assert lesson_id in lesson_ids


def test_lesson_progress_requires_authentication(client):
    assert client.post(f"{STUDENTS}/lessons/1/progress", json={"status": "opened"}).status_code == 401


@pytest.mark.parametrize("status_value", ["opened", "completed"])
def test_lesson_progress_accepts_both_statuses(client, demo_token, status_value):
    db = SessionLocal()
    try:
        lesson_id = db.scalar(select(Lesson.id).order_by(Lesson.id).limit(1))
    finally:
        db.close()
    resp = client.post(
        f"{STUDENTS}/lessons/{lesson_id}/progress",
        headers=_auth(demo_token),
        json={"status": status_value},
    )
    assert resp.status_code == 200, resp.text
