"""Student API tests: own profile, progress and preferences, with cross-user isolation checks."""

from datetime import datetime, timezone

from sqlalchemy import delete, select

from app.core.database import SessionLocal
from app.models import Lesson, LessonProgress, UserPreference

BASE = "/api/students"


def _auth(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _get_ok(client, token: str, path: str):
    resp = client.get(path, headers=_auth(token))
    assert resp.status_code == 200, f"{path}: {resp.text}"
    return resp.json()


def _first_lesson_id() -> int:
    db = SessionLocal()
    try:
        lesson_id = db.scalar(select(Lesson.id).order_by(Lesson.id).limit(1))
    finally:
        db.close()
    assert lesson_id is not None
    return lesson_id


def test_profile_requires_authentication(client):
    assert client.get(f"{BASE}/me").status_code == 401


def test_profile_denied_for_teacher(client, token_for):
    resp = client.get(f"{BASE}/me", headers=_auth(token_for("iso_teacher")))
    assert resp.status_code == 403


def test_profile_for_demo_student(client, demo_token):
    body = _get_ok(client, demo_token, f"{BASE}/me")
    assert body["username"] == "demo_student"
    # The seeded label is "Class 8 / ತರಗತಿ 8", so check containment rather than equality.
    assert body["class_label"] is not None
    assert "Class 8" in body["class_label"]
    assert body["board_name_kn"] is not None


def test_progress_shape_for_demo_student(client, demo_token):
    body = _get_ok(client, demo_token, f"{BASE}/progress")
    assert isinstance(body["lesson_progress"], list)
    assert isinstance(body["quiz_attempts_list"], list)
    assert isinstance(body["lessons_opened"], int)
    assert isinstance(body["lessons_completed"], int)
    assert isinstance(body["quiz_attempts"], int)
    assert body["lessons_opened"] == len(body["lesson_progress"])
    assert body["quiz_attempts"] == len(body["quiz_attempts_list"])


def test_progress_is_scoped_to_token_owner(client, token_for, demo_token, isolation_users):
    lesson_id = _first_lesson_id()
    student_a_id = isolation_users["iso_student_a"]
    now = datetime.now(timezone.utc)

    db = SessionLocal()
    try:
        db.add(
            LessonProgress(
                user_id=student_a_id,
                lesson_id=lesson_id,
                status="completed",
                opened_at=now,
                completed_at=now,
                time_spent_seconds=60,
            )
        )
        db.commit()

        a = _get_ok(client, token_for("iso_student_a"), f"{BASE}/progress")
        assert any(row["lesson_id"] == lesson_id for row in a["lesson_progress"])
        assert a["lessons_completed"] >= 1

        b = _get_ok(client, token_for("iso_student_b"), f"{BASE}/progress")
        assert not any(row["lesson_id"] == lesson_id for row in b["lesson_progress"])

        demo = _get_ok(client, demo_token, f"{BASE}/progress")
        assert not any(row["lesson_id"] == lesson_id for row in demo["lesson_progress"])
    finally:
        db.execute(
            delete(LessonProgress).where(
                LessonProgress.user_id == student_a_id,
                LessonProgress.lesson_id == lesson_id,
            )
        )
        db.commit()
        db.close()



def test_preferences_are_scoped_to_token_owner(client, token_for, isolation_users):
    student_a_id = isolation_users["iso_student_a"]

    db = SessionLocal()
    try:
        # user_id is unique on user_preferences, so each user holds at most one preference row.
        db.add(UserPreference(user_id=student_a_id, key="font_size", value="large"))
        db.commit()

        a = _get_ok(client, token_for("iso_student_a"), f"{BASE}/preferences")
        assert [item["key"] for item in a] == ["font_size"]
        assert a[0]["value"] == "large"

        b = _get_ok(client, token_for("iso_student_b"), f"{BASE}/preferences")
        assert not any(item["key"] == "font_size" for item in b)
    finally:
        db.execute(delete(UserPreference).where(UserPreference.user_id == student_a_id))
        db.commit()
        db.close()


def test_client_cannot_pass_user_id_in_path(client, demo_token, isolation_users):
    user_id = isolation_users["iso_student_a"]
    resp = client.get(f"{BASE}/{user_id}/progress", headers=_auth(demo_token))
    assert resp.status_code in (404, 405)


def test_teacher_denied_progress_and_preferences(client, token_for):
    teacher = token_for("iso_teacher")
    assert client.get(f"{BASE}/progress", headers=_auth(teacher)).status_code == 403
    assert client.get(f"{BASE}/preferences", headers=_auth(teacher)).status_code == 403
