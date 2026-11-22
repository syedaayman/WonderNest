"""Gemini powered AI tutor endpoints.

The student identity comes from the JWT access token only: the request body can carry the
lesson context and the conversation id, never a user id. The Gemini API key stays in the
backend process.
"""

import logging
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.core.config import get_settings
from app.core.database import get_db
from app.models import AIConversation, AIMessage, Chapter, LearningObjective, Lesson, Topic, User
from app.schemas.ai_tutor import (
    SuggestedPrompt,
    SuggestedPromptsOut,
    TutorChatRequest,
    TutorChatResponse,
    TutorStatusOut,
    TutorUsage,
)
from app.services import ai_tutor_service
from app.services.ai_tutor_service import TutorContext, TutorError

logger = logging.getLogger("wondernest.ai")

router = APIRouter(prefix="/api/ai/tutor", tags=["ai-tutor"])

SUGGESTED_PROMPTS: tuple[SuggestedPrompt, ...] = (
    SuggestedPrompt(
        id="photosynthesis-kn",
        label="Explain photosynthesis in Kannada",
        label_kn="ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆ ವಿವರಿಸಿ",
        prompt="Explain photosynthesis in Kannada with a simple example.",
        language="kn",
        topic="Photosynthesis",
    ),
    SuggestedPrompt(
        id="water-cycle",
        label="Teach me the water cycle",
        label_kn="ಜಲ ಚಕ್ರ ಕಲಿಸಿ",
        prompt="Teach me the water cycle step by step with an everyday example.",
        language="en",
        topic="Water cycle",
    ),
    SuggestedPrompt(
        id="force-examples",
        label="What is force? Give examples",
        label_kn="ಬಲ ಎಂದರೇನು?",
        prompt="What is force? Give three examples I can see every day.",
        language="en",
        topic="Force",
    ),
    SuggestedPrompt(
        id="friction-kn",
        label="Explain friction in simple Kannada",
        label_kn="ಘರ್ಷಣೆ ಸರಳವಾಗಿ",
        prompt="Explain friction in simple Kannada with an example from riding a bicycle.",
        language="kn",
        topic="Friction",
    ),
    SuggestedPrompt(
        id="practice-questions",
        label="Give me five practice questions",
        label_kn="ಐದು ಅಭ್ಯಾಸ ಪ್ರಶ್ನೆಗಳು",
        prompt="Give me five practice questions on this chapter. Give hints, not the answers.",
        language="en",
        topic="Practice",
    ),
    SuggestedPrompt(
        id="explain-age-13",
        label="Explain this lesson like I am 13",
        label_kn="ಹದಿಮೂರನೇ ವಯಸ್ಸಿನಂತೆ ವಿವರಿಸಿ",
        prompt="Explain this lesson like I am 13 years old.",
        language="en",
        topic="Lesson",
    ),
)


def _not_found(what: str) -> HTTPException:
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{what} not found.")


def _load_context(
    db: Session,
    *,
    chapter_id: int | None,
    topic_id: int | None,
    lesson_id: int | None,
) -> tuple[TutorContext, int | None, int | None]:
    """Resolve the optional chapter/topic/lesson ids into tutor context.

    Ids supplied by the client are validated against the database, so a bad id is a clear
    404 instead of a silently ignored parameter.
    """
    chapter: Chapter | None = None
    topic: Topic | None = None
    lesson: Lesson | None = None

    if lesson_id is not None:
        lesson = db.get(Lesson, lesson_id)
        if lesson is None:
            raise _not_found("Lesson")
        topic = db.get(Topic, lesson.topic_id)
    elif topic_id is not None:
        topic = db.get(Topic, topic_id)
        if topic is None:
            raise _not_found("Topic")
        lesson = db.scalar(select(Lesson).where(Lesson.topic_id == topic.id))

    if topic is not None:
        chapter = db.get(Chapter, topic.chapter_id)
    elif chapter_id is not None:
        chapter = db.get(Chapter, chapter_id)
        if chapter is None:
            raise _not_found("Chapter")
        topic = db.scalar(
            select(Topic).where(Topic.chapter_id == chapter.id).order_by(Topic.order).limit(1)
        )
        if topic is not None:
            lesson = db.scalar(select(Lesson).where(Lesson.topic_id == topic.id))

    if chapter_id is not None and chapter is not None and chapter.id != chapter_id:
        raise _not_found("Chapter")

    objectives: list[str] = []
    if topic is not None:
        objectives = [
            row.text_kn
            for row in db.scalars(
                select(LearningObjective)
                .where(LearningObjective.topic_id == topic.id)
                .order_by(LearningObjective.position)
            ).all()
        ]

    key_terms: list[str] = []
    if lesson is not None:
        for term in lesson.key_terms or []:
            label = " / ".join(
                part for part in (term.get("kn", ""), term.get("en", "")) if part
            )
            if label:
                key_terms.append(label)

    context = TutorContext(
        chapter_title_kn=chapter.title_kn if chapter else None,
        chapter_title_en=chapter.title_en if chapter else None,
        topic_title_kn=topic.title_kn if topic else None,
        topic_title_en=topic.title_en if topic else None,
        lesson_body=lesson.body_kn if lesson else None,
        key_terms=key_terms,
        objectives=objectives,
    )
    return (
        context,
        chapter.id if chapter else None,
        topic.id if topic else None,
    )


def _history_from_db(db: Session, conversation_id: int, limit: int) -> list[dict[str, str]]:
    rows = db.scalars(
        select(AIMessage)
        .where(AIMessage.conversation_id == conversation_id)
        .order_by(AIMessage.id.desc())
        .limit(limit)
    ).all()
    return [
        {"role": row.role, "content": row.content}
        for row in reversed(rows)
    ]


@router.get("/status", response_model=TutorStatusOut)
def tutor_status(user: User = Depends(get_current_user)) -> TutorStatusOut:
    """Report whether the backend holds a Gemini key, without ever exposing it."""
    settings = get_settings()
    configured = ai_tutor_service.is_configured()
    return TutorStatusOut(
        configured=configured,
        model=ai_tutor_service.configured_model(),
        message=(
            "Gemini is connected and ready."
            if configured
            else "GEMINI_API_KEY is not set on the server, so the tutor cannot answer yet."
        ),
        rate_limit_requests=settings.AI_RATE_LIMIT_REQUESTS,
        rate_limit_window_seconds=settings.AI_RATE_LIMIT_WINDOW_SECONDS,
        max_message_chars=settings.AI_MAX_MESSAGE_CHARS,
    )


@router.get("/suggestions", response_model=SuggestedPromptsOut)
def tutor_suggestions(user: User = Depends(get_current_user)) -> SuggestedPromptsOut:
    return SuggestedPromptsOut(prompts=list(SUGGESTED_PROMPTS))


@router.post("/chat", response_model=TutorChatResponse)
async def tutor_chat(
    body: TutorChatRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> TutorChatResponse:
    """Answer a student question with Gemini, grounded in the optional lesson context."""
    settings = get_settings()

    if not ai_tutor_service.is_configured():
        error = ai_tutor_service.AINotConfiguredError()
        raise HTTPException(
            status_code=error.status_code,
            detail={"code": error.code, "message": error.message},
        )

    message = body.message.strip()
    if not message:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={"code": "empty_message", "message": "Please type a question first."},
        )
    if len(message) > settings.AI_MAX_MESSAGE_CHARS:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail={
                "code": "message_too_long",
                "message": f"Please keep your question under {settings.AI_MAX_MESSAGE_CHARS} characters.",
            },
        )

    wait_for = ai_tutor_service.rate_limiter.check(
        f"tutor:{user.id}",
        settings.AI_RATE_LIMIT_REQUESTS,
        settings.AI_RATE_LIMIT_WINDOW_SECONDS,
    )
    if wait_for is not None:
        retry_after = int(wait_for) + 1
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail={
                "code": "ai_rate_limited",
                "message": (
                    "You have sent several questions quickly. "
                    f"Please wait {retry_after} seconds and try again."
                ),
            },
            headers={"Retry-After": str(retry_after)},
        )

    context, chapter_id, topic_id = _load_context(
        db, chapter_id=body.chapter_id, topic_id=body.topic_id, lesson_id=body.lesson_id
    )

    conversation: AIConversation | None = None
    history: list[dict[str, str]] = []
    if body.conversation_id is not None:
        conversation = db.scalar(
            select(AIConversation).where(
                AIConversation.id == body.conversation_id,
                AIConversation.user_id == user.id,
            )
        )
        if conversation is None:
            raise _not_found("Conversation")
        history = _history_from_db(db, conversation.id, settings.AI_MAX_HISTORY_MESSAGES)

    if conversation is None:
        conversation = AIConversation(
            user_id=user.id, chapter_id=chapter_id, topic_id=topic_id
        )
        db.add(conversation)
        db.flush()
        # A brand new conversation has no stored turns, so accept client history once.
        history = [
            {"role": turn.role, "content": turn.content}
            for turn in body.history[-settings.AI_MAX_HISTORY_MESSAGES :]
        ]

    db.add(
        AIMessage(
            conversation_id=conversation.id,
            role="user",
            content=message,
            created_at=datetime.now(timezone.utc),
        )
    )
    db.commit()
    conversation_id = conversation.id

    try:
        reply = await ai_tutor_service.generate_tutor_reply(
            message=message,
            language=body.language,
            level=body.level,
            context=context,
            history=history,
            user_id=user.id,
        )
    except TutorError as exc:
        logger.warning(
            "ai_tutor_error user_id=%s code=%s status=%s conversation_id=%s",
            user.id,
            exc.code,
            exc.status_code,
            conversation_id,
        )
        headers = {"Retry-After": str(exc.retry_after)} if exc.retry_after else None
        raise HTTPException(
            status_code=exc.status_code,
            detail={"code": exc.code, "message": exc.message},
            headers=headers,
        ) from exc

    db.add(
        AIMessage(
            conversation_id=conversation_id,
            role="assistant",
            content=reply.text,
            mode="live",
            created_at=datetime.now(timezone.utc),
        )
    )
    db.commit()

    return TutorChatResponse(
        reply=reply.text,
        conversation_id=conversation_id,
        model=reply.model,
        language=body.language,
        latency_ms=reply.latency_ms,
        usage=TutorUsage(**reply.usage) if reply.usage else None,
    )
