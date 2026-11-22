"""Voice input: transcribe a short spoken question with Gemini.

The browser records a clip and sends it base64 encoded, so no multipart dependency is needed
and the Gemini key never leaves the backend. The transcript is returned to the student for
review before they send it, so a misheard word is never submitted silently.
"""

import base64
import binascii
import logging

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps import get_current_user
from app.core.config import get_settings
from app.models import User
from app.schemas.voice import TranscribeRequest, TranscribeResponse
from app.services import ai_tutor_service
from app.services.ai_tutor_service import TutorError

logger = logging.getLogger("wondernest.ai")

router = APIRouter(prefix="/api/ai/tutor", tags=["ai-tutor"])

ALLOWED_MIME = {
    "audio/webm",
    "audio/ogg",
    "audio/wav",
    "audio/x-wav",
    "audio/mp4",
    "audio/mpeg",
    "audio/aac",
}


@router.post("/transcribe", response_model=TranscribeResponse)
async def transcribe(
    body: TranscribeRequest,
    user: User = Depends(get_current_user),
) -> TranscribeResponse:
    """Turn a spoken Kannada or English question into text for the student to edit."""
    settings = get_settings()

    if not ai_tutor_service.is_configured():
        error = ai_tutor_service.AINotConfiguredError()
        raise HTTPException(
            status_code=error.status_code,
            detail={"code": error.code, "message": error.message},
        )

    mime = body.mime_type.split(";")[0].strip().lower()
    if mime not in ALLOWED_MIME:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "code": "unsupported_audio",
                "message": "That audio format is not supported. Please record again.",
            },
        )

    wait_for = ai_tutor_service.rate_limiter.check(
        f"transcribe:{user.id}",
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
                    "You have used the microphone several times quickly. "
                    f"Please wait {retry_after} seconds and try again."
                ),
            },
            headers={"Retry-After": str(retry_after)},
        )

    try:
        audio = base64.b64decode(body.audio_base64, validate=True)
    except (binascii.Error, ValueError) as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "code": "invalid_audio",
                "message": "The recording could not be read. Please record again.",
            },
        ) from exc

    if not audio:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"code": "invalid_audio", "message": "The recording was empty."},
        )

    try:
        text, model = await ai_tutor_service.transcribe_audio(
            audio=audio, mime_type=mime, language=body.language
        )
    except TutorError as exc:
        logger.warning(
            "ai_transcribe_error user_id=%s code=%s status=%s bytes=%s",
            user.id,
            exc.code,
            exc.status_code,
            len(audio),
        )
        headers = {"Retry-After": str(exc.retry_after)} if exc.retry_after else None
        raise HTTPException(
            status_code=exc.status_code,
            detail={"code": exc.code, "message": exc.message},
            headers=headers,
        ) from exc

    return TranscribeResponse(text=text, model=model)
