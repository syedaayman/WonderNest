"""Exam preparation endpoint: chapter-specific practice questions with model answers.

The questions are WonderNest's own practice material. The response always carries a
``source_note`` so the UI can state that these are practice questions, not a prediction of
what an examination paper will contain.
"""

from fastapi import APIRouter, Depends, HTTPException, Path, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.core.database import get_db
from app.curriculum import exam as exam_content
from app.models import Chapter, PracticeQuestion, User
from app.schemas.exam import ExamQuestionOut, ExamQuestionsOut, ExamTypeOut

router = APIRouter(prefix="/api/curriculum", tags=["exam"])

SOURCE_NOTE = (
    "Important practice questions written by WonderNest for this chapter. They are for "
    "revision only and are not a prediction of examination questions, and they are not "
    "official textbook or guidebook content."
)

# Order the type chips the way a student revises: recall first, long answers last.
_TYPE_ORDER = (
    "very_short",
    "short",
    "long",
    "mcq",
    "fill_blank",
    "true_false",
    "diagram",
    "concept",
)


def _with_ids(items: list[dict]) -> list[dict]:
    """Give every question a stable id so the client can track revealed/revision state."""
    for index, item in enumerate(items):
        item.setdefault("id", f"q{index + 1}")
    return items


def _ordered(items: list[dict]) -> list[dict]:
    def key(item: dict) -> tuple[int, int]:
        qtype = item.get("type", "concept")
        position = _TYPE_ORDER.index(qtype) if qtype in _TYPE_ORDER else len(_TYPE_ORDER)
        return (position, item.get("difficulty", 1) or 1)

    return sorted(items, key=key)


@router.get("/chapters/{chapter_id}/exam", response_model=ExamQuestionsOut)
def get_chapter_exam(
    chapter_id: int = Path(ge=1),
    question_type: str | None = Query(default=None, alias="type"),
    _user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> ExamQuestionsOut:
    """Exam practice for one chapter.

    A chapter with an authored bank uses it; every other chapter falls back to its own
    practice quiz, so no chapter ever shows another chapter's questions.
    """
    chapter = db.scalar(select(Chapter).where(Chapter.id == chapter_id))
    if chapter is None:
        raise HTTPException(status_code=404, detail="Chapter not found.")

    bank = exam_content.bank_for(chapter.number)
    if bank:
        items = [dict(item) for item in bank]
    else:
        quiz_rows = db.scalars(
            select(PracticeQuestion)
            .where(PracticeQuestion.chapter_id == chapter_id)
            .order_by(PracticeQuestion.id)
        ).all()
        items = exam_content.questions_from_quiz(quiz_rows)

    items = _ordered(_with_ids(items))

    counts = exam_content.summarise(items)
    types = [
        ExamTypeOut(
            key=key,
            label_en=exam_content.EXAM_TYPE_LABELS.get(key, {}).get("en", key.replace("_", " ").title()),
            label_kn=exam_content.EXAM_TYPE_LABELS.get(key, {}).get("kn", ""),
            count=count,
        )
        for key, count in sorted(
            counts.items(),
            key=lambda pair: _TYPE_ORDER.index(pair[0]) if pair[0] in _TYPE_ORDER else 99,
        )
    ]

    if question_type:
        items = [item for item in items if item.get("type") == question_type]

    return ExamQuestionsOut(
        chapter_id=chapter.id,
        chapter_number=chapter.number,
        source_note=SOURCE_NOTE,
        total=len(items),
        types=types,
        questions=[
            ExamQuestionOut(
                id=item["id"],
                type=item.get("type", "concept"),
                marks=int(item.get("marks", 1) or 1),
                difficulty=int(item.get("difficulty", 1) or 1),
                question_en=item.get("question_en", ""),
                question_kn=item.get("question_kn", "") or item.get("question_en", ""),
                answer_en=item.get("answer_en", ""),
                answer_kn=item.get("answer_kn", "") or item.get("answer_en", ""),
                explanation_en=item.get("explanation_en", ""),
                explanation_kn=item.get("explanation_kn", "")
                or item.get("explanation_en", ""),
                options_en=list(item.get("options_en") or []),
                options_kn=list(item.get("options_kn") or []),
                correct_index=item.get("correct_index"),
            )
            for item in items
        ],
    )
