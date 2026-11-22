"""Idempotent seeding of the curriculum and the demo student.

Running ``seed_curriculum`` repeatedly never creates duplicate rows: every entity is looked up by
its natural key and updated in place when it already exists. Everything runs in one transaction.

The curriculum content itself lives in :mod:`app.curriculum.units` and is original WonderNest
study material. Chapter, topic, lesson and question identities are unchanged, so existing student
progress, quiz attempts and mistakes keep pointing at the same rows.
"""

from typing import Any

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.curriculum import seed_data as data
from app.curriculum import units as curriculum
from app.models.curriculum import (
    Board,
    Chapter,
    ClassLevel,
    Language,
    LearningObjective,
    Lesson,
    PracticeQuestion,
    Subject,
    Topic,
)
from app.models.learning import QuizAttempt
from app.models.user import LearnerProfile, User
from app.security.passwords import hash_password


def _get_or_create(db: Session, model: Any, lookup: dict[str, Any], values: dict[str, Any]) -> Any:
    """Return the row matching ``lookup``, creating it if missing, and apply ``values`` to it."""
    obj = db.scalar(select(model).filter_by(**lookup))
    if obj is None:
        obj = model(**lookup, **values)
        db.add(obj)
        db.flush()
    else:
        for key, value in values.items():
            setattr(obj, key, value)
    return obj


def _drop_stale_sample_chapters(db: Session, subject_id: int, keep_numbers: set[int]) -> int:
    """Delete sample chapters that are no longer part of the curriculum.

    A chapter that already holds quiz attempts is kept: removing it would cascade-delete the
    student's own history, which the project must never do silently.
    """
    stale = db.scalars(
        select(Chapter).where(
            Chapter.subject_id == subject_id,
            Chapter.is_sample.is_(True),
            Chapter.number.notin_(keep_numbers),
        )
    ).all()
    removed = 0
    for chapter in stale:
        attempts = db.scalar(
            select(func.count()).select_from(QuizAttempt).where(QuizAttempt.chapter_id == chapter.id)
        ) or 0
        if attempts:
            continue
        db.delete(chapter)
        removed += 1
    db.flush()
    return removed


def seed_curriculum(db: Session, demo_password: str) -> dict[str, int]:
    """Seed languages, the Class 8 Science curriculum and the demo student in one transaction."""
    try:
        for lang in data.LANGUAGES:
            _get_or_create(
                db,
                Language,
                {"code": lang["code"]},
                {"name_en": lang["name_en"], "name_native": lang["name_native"]},
            )

        board = _get_or_create(
            db,
            Board,
            {"code": data.BOARD["code"]},
            {
                "name_en": data.BOARD["name_en"],
                "name_kn": data.BOARD["name_kn"],
                "is_active": data.BOARD["is_active"],
            },
        )

        class_level = _get_or_create(
            db,
            ClassLevel,
            {"board_id": board.id, "level_number": data.CLASS_LEVEL["level_number"]},
            {"label": data.CLASS_LEVEL["label"]},
        )

        subject = _get_or_create(
            db,
            Subject,
            {"class_id": class_level.id, "code": data.SUBJECT["code"]},
            {"title_en": data.SUBJECT["title_en"], "title_kn": data.SUBJECT["title_kn"]},
        )

        chapter_count = 0
        topic_count = 0
        lesson_count = 0
        question_count = 0
        seeded_topic_ids: list[int] = []

        for unit in curriculum.UNITS:
            chapter = _get_or_create(
                db,
                Chapter,
                {"subject_id": subject.id, "number": unit["number"]},
                {
                    "title_kn": unit["title_kn"],
                    "title_en": unit["title_en"],
                    "summary_kn": unit["summary_kn"],
                    "summary_en": unit["summary_en"],
                    "category": unit["category"],
                    "is_enrichment": unit["is_enrichment"],
                    "visualizations": list(unit["visualizations"]),
                    "notes_kn": list(unit["notes_kn"]),
                    "notes_en": list(unit["notes_en"]),
                    "videos": list(unit["videos"]),
                    "estimated_minutes": unit["estimated_minutes"],
                    "is_sample": True,
                    "source_note": curriculum.SOURCE_NOTE,
                },
            )
            chapter_count += 1

            for order, topic_data in enumerate(unit["topics"], start=1):
                topic = _get_or_create(
                    db,
                    Topic,
                    {"chapter_id": chapter.id, "order": order},
                    {"title_kn": topic_data["title_kn"], "title_en": topic_data["title_en"]},
                )
                topic_count += 1
                seeded_topic_ids.append(topic.id)

                objectives_kn = topic_data.get("objectives_kn") or []
                objectives_en = topic_data.get("objectives_en") or []
                for position, text_kn in enumerate(objectives_kn, start=1):
                    _get_or_create(
                        db,
                        LearningObjective,
                        {"topic_id": topic.id, "position": position},
                        {
                            "text_kn": text_kn,
                            "text_en": (
                                objectives_en[position - 1]
                                if position - 1 < len(objectives_en)
                                else None
                            ),
                        },
                    )

                _get_or_create(
                    db,
                    Lesson,
                    {"topic_id": topic.id},
                    {
                        "body_kn": "\n\n".join(topic_data["body_kn"]),
                        "body_en": "\n\n".join(topic_data["body_en"]),
                        "key_terms": list(topic_data["key_terms"]),
                        "example_kn": topic_data["example_kn"],
                        "example_en": topic_data["example_en"],
                        "is_sample": True,
                        "source_note": curriculum.SOURCE_NOTE,
                    },
                )
                lesson_count += 1

            # Quiz questions belong to the chapter, and to its first topic so the tutor and the
            # mistake tracker still have a topic to attach revision hints to.
            primary_topic_id = db.scalar(
                select(Topic.id)
                .where(Topic.chapter_id == chapter.id)
                .order_by(Topic.order)
                .limit(1)
            )
            for question_data in unit["quiz"]:
                _get_or_create(
                    db,
                    PracticeQuestion,
                    {"chapter_id": chapter.id, "question_kn": question_data["question_kn"]},
                    {
                        "topic_id": primary_topic_id,
                        "question_type": question_data.get("question_type", "mcq"),
                        "question_en": question_data["question_en"],
                        "options_kn": list(question_data["options_kn"]),
                        "options_en": list(question_data["options_en"]),
                        "correct_index": question_data["correct_index"],
                        "explanation_kn": question_data["explanation_kn"],
                        "explanation_en": question_data["explanation_en"],
                        "difficulty": question_data["difficulty"],
                    },
                )
                question_count += 1

        removed = _drop_stale_sample_chapters(
            db, subject.id, {unit["number"] for unit in curriculum.UNITS}
        )

        demo = data.DEMO_STUDENT
        student = db.scalar(select(User).where(User.username == demo["username"]))
        students_count = 0
        if student is None:
            student = User(
                username=demo["username"],
                password_hash=hash_password(demo_password),
                display_name=demo["display_name"],
                role=demo["role"],
                preferred_language=demo["preferred_language"],
            )
            db.add(student)
            db.flush()
        students_count += 1

        _get_or_create(
            db,
            LearnerProfile,
            {"user_id": student.id},
            {
                "class_id": class_level.id,
                "board_id": board.id,
                "language_code": "kn",
                "daily_goal_minutes": demo["daily_goal_minutes"],
            },
        )

        # learning_objectives counts ALL LearningObjective rows belonging to the topics seeded in
        # this run (created or pre-existing), not only rows newly inserted in this run.
        objective_count = db.scalar(
            select(func.count())
            .select_from(LearningObjective)
            .where(LearningObjective.topic_id.in_(seeded_topic_ids))
        ) or 0

        db.commit()
    except Exception:
        db.rollback()
        raise

    return {
        "boards": 1,
        "classes": 1,
        "subjects": 1,
        "chapters": chapter_count,
        "topics": topic_count,
        "lessons": lesson_count,
        "questions": question_count,
        "students_created_or_existing": students_count,
        "learning_objectives": objective_count,
        "stale_chapters_removed": removed,
    }
