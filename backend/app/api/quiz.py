"""Chapter quiz endpoints: fetch questions without answers, submit an attempt, read results."""

from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import require_roles
from app.core.database import get_db
from app.models import Chapter, MistakeRecord, PracticeQuestion, QuizAnswer, QuizAttempt, User
from app.schemas.quiz import (
    QuizAnswerResultOut,
    QuizOut,
    QuizQuestionOut,
    QuizResultOut,
    QuizSubmitRequest,
)

router = APIRouter(prefix="/api/quiz", tags=["quiz"])


def _chapter_or_404(db: Session, chapter_id: int) -> Chapter:
    chapter = db.get(Chapter, chapter_id)
    if chapter is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chapter not found.")
    return chapter


def _questions(db: Session, chapter_id: int) -> list[PracticeQuestion]:
    return list(
        db.scalars(
            select(PracticeQuestion)
            .where(PracticeQuestion.chapter_id == chapter_id)
            .order_by(PracticeQuestion.difficulty, PracticeQuestion.id)
        ).all()
    )


@router.get("/chapters/{chapter_id}", response_model=QuizOut)
def get_chapter_quiz(
    chapter_id: int = Path(ge=1),
    _user: User = Depends(require_roles("student")),
    db: Session = Depends(get_db),
) -> QuizOut:
    chapter = _chapter_or_404(db, chapter_id)
    questions = _questions(db, chapter_id)
    if not questions:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No practice questions for this chapter yet.",
        )
    return QuizOut(
        chapter_id=chapter.id,
        chapter_title_kn=chapter.title_kn,
        chapter_title_en=chapter.title_en,
        total=len(questions),
        questions=[
            QuizQuestionOut(
                id=question.id,
                question_type=question.question_type,
                question_kn=question.question_kn,
                options_kn=list(question.options_kn or []),
                difficulty=question.difficulty,
            )
            for question in questions
        ],
    )


def _result_payload(
    db: Session,
    attempt: QuizAttempt,
    chapter: Chapter,
    questions: list[PracticeQuestion],
    selected: dict[int, int | None],
) -> QuizResultOut:
    results = [
        QuizAnswerResultOut(
            question_id=question.id,
            selected_index=selected.get(question.id),
            correct_index=question.correct_index,
            is_correct=selected.get(question.id) == question.correct_index,
            explanation_kn=question.explanation_kn,
            question_kn=question.question_kn,
        )
        for question in questions
    ]
    return QuizResultOut(
        attempt_id=attempt.id,
        chapter_id=chapter.id,
        chapter_title_kn=chapter.title_kn,
        score=attempt.score,
        total=attempt.total,
        created_at=attempt.created_at,
        answers=results,
    )


@router.post(
    "/chapters/{chapter_id}/attempts",
    response_model=QuizResultOut,
    status_code=status.HTTP_201_CREATED,
)
def submit_attempt(
    body: QuizSubmitRequest,
    chapter_id: int = Path(ge=1),
    user: User = Depends(require_roles("student")),
    db: Session = Depends(get_db),
) -> QuizResultOut:
    """Score the submitted answers, store the attempt and record the student's mistakes."""
    chapter = _chapter_or_404(db, chapter_id)
    questions = _questions(db, chapter_id)
    if not questions:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No practice questions for this chapter yet.",
        )

    by_id = {question.id: question for question in questions}
    selected: dict[int, int | None] = {}
    for answer in body.answers:
        question = by_id.get(answer.question_id)
        if question is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Question {answer.question_id} does not belong to this chapter.",
            )
        options = list(question.options_kn or [])
        if answer.selected_index is not None and answer.selected_index >= len(options):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Answer index out of range for question {answer.question_id}.",
            )
        selected[question.id] = answer.selected_index

    score = sum(1 for question in questions if selected.get(question.id) == question.correct_index)
    attempt = QuizAttempt(
        user_id=user.id, chapter_id=chapter.id, score=score, total=len(questions)
    )
    db.add(attempt)
    db.flush()

    now = datetime.now(timezone.utc)
    for question in questions:
        is_correct = selected.get(question.id) == question.correct_index
        db.add(
            QuizAnswer(
                attempt_id=attempt.id,
                question_id=question.id,
                selected_index=selected.get(question.id),
                is_correct=is_correct,
            )
        )
        if is_correct:
            continue
        mistake = db.scalar(
            select(MistakeRecord).where(
                MistakeRecord.user_id == user.id,
                MistakeRecord.question_id == question.id,
            )
        )
        if mistake is None:
            db.add(
                MistakeRecord(
                    user_id=user.id,
                    topic_id=question.topic_id,
                    question_id=question.id,
                    count=1,
                    last_seen_at=now,
                )
            )
        else:
            mistake.count += 1
            mistake.last_seen_at = now

    db.commit()
    db.refresh(attempt)
    return _result_payload(db, attempt, chapter, questions, selected)


@router.get("/attempts/{attempt_id}", response_model=QuizResultOut)
def get_attempt(
    attempt_id: int = Path(ge=1),
    user: User = Depends(require_roles("student")),
    db: Session = Depends(get_db),
) -> QuizResultOut:
    attempt = db.scalar(
        select(QuizAttempt).where(QuizAttempt.id == attempt_id, QuizAttempt.user_id == user.id)
    )
    if attempt is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Attempt not found.")
    chapter = _chapter_or_404(db, attempt.chapter_id)
    questions = _questions(db, attempt.chapter_id)
    stored = db.scalars(
        select(QuizAnswer).where(QuizAnswer.attempt_id == attempt.id)
    ).all()
    selected = {row.question_id: row.selected_index for row in stored}
    return _result_payload(db, attempt, chapter, questions, selected)
