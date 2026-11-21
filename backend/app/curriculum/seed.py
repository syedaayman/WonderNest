"""Idempotent seeding of the sample curriculum and the demo student.

Running ``seed_curriculum`` repeatedly never creates duplicate rows: every entity is looked up by
its natural key and updated in place when it already exists. Everything runs in one transaction.
"""

from typing import Any

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.curriculum import seed_data as data
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


def seed_curriculum(db: Session, demo_password: str) -> dict[str, int]:
    """Seed languages, the sample Class 8 Science curriculum and the demo student in one transaction."""
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

        for chapter_data in data.CHAPTERS:
            chapter = _get_or_create(
                db,
                Chapter,
                {"subject_id": subject.id, "number": chapter_data["number"]},
                {
                    "title_kn": chapter_data["title_kn"],
                    "title_en": chapter_data["title_en"],
                    "summary_kn": chapter_data["summary_kn"],
                    "estimated_minutes": chapter_data["estimated_minutes"],
                    "is_sample": True,
                    "source_note": data.SAMPLE_NOTE,
                },
            )
            chapter_count += 1

            for topic_data in chapter_data["topics"]:
                topic = _get_or_create(
                    db,
                    Topic,
                    {"chapter_id": chapter.id, "order": topic_data["order"]},
                    {"title_kn": topic_data["title_kn"], "title_en": topic_data["title_en"]},
                )
                topic_count += 1
                seeded_topic_ids.append(topic.id)

                # Objectives are upserted by (topic_id, position). Objectives removed from seed_data
                # are deliberately NOT deleted automatically; remove stale rows by hand if needed.
                for position, text in enumerate(topic_data.get("objectives_kn", []), start=1):
                    _get_or_create(
                        db,
                        LearningObjective,
                        {"topic_id": topic.id, "position": position},
                        {"text_kn": text},
                    )

                lesson_data = topic_data["lesson"]
                _get_or_create(
                    db,
                    Lesson,
                    {"topic_id": topic.id},
                    {
                        "body_kn": lesson_data["body_kn"],
                        "key_terms": lesson_data["key_terms"],
                        "example_kn": lesson_data["example_kn"],
                        "is_sample": True,
                        "source_note": data.SAMPLE_NOTE,
                    },
                )
                lesson_count += 1

                for question_data in topic_data["practice"]:
                    _get_or_create(
                        db,
                        PracticeQuestion,
                        {"chapter_id": chapter.id, "question_kn": question_data["question_kn"]},
                        {
                            "topic_id": topic.id,
                            "question_type": question_data["question_type"],
                            "options_kn": question_data["options_kn"],
                            "correct_index": question_data["correct_index"],
                            "explanation_kn": question_data["explanation_kn"],
                            "difficulty": question_data["difficulty"],
                        },
                    )
                    question_count += 1

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
    }
