"""Diagram narration endpoint.

The Gemini key stays in the backend: the browser posts the diagram explanation it is looking
at and receives audio bytes. When no TTS model is reachable the endpoint answers 503 with a
machine readable reason so the client can explain it and fall back to the device voice instead
of pretending audio was generated.
"""

import base64
import logging

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps import get_current_user
from app.core.config import get_settings
from app.models import User
from app.schemas.narration import NarrationAudioOut, NarrationRequest, NarrationStatusOut
from app.services import ai_tutor_service, narration_service
from app.services.narration_service import NarrationError

logger = logging.getLogger("wondernest.narration")

router = APIRouter(prefix="/api/narration", tags=["narration"])

NARRATION_RATE_LIMIT = 20


@router.get("/status", response_model=NarrationStatusOut)
async def narration_status(_user: User = Depends(get_current_user)) -> NarrationStatusOut:
    """Tell the client whether real speech generation is possible for this project."""
    result = await narration_service.status()
    return NarrationStatusOut(
        available=result.available,
        model=result.model,
        reason=result.reason,
        detail=result.detail,
    )


@router.post("/speak", response_model=NarrationAudioOut)
async def speak(
    body: NarrationRequest,
    user: User = Depends(get_current_user),
) -> NarrationAudioOut:
    """Speak one diagram explanation in Kannada or English."""
    settings = get_settings()
    wait_for = ai_tutor_service.rate_limiter.check(
        f"narration:{user.id}",
        NARRATION_RATE_LIMIT,
        settings.AI_RATE_LIMIT_WINDOW_SECONDS,
    )
    if wait_for is not None:
        retry_after = int(wait_for) + 1
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail={
                "code": "tts_rate_limited",
                "message": f"Too many narration requests. Please wait {retry_after} seconds.",
            },
            headers={"Retry-After": str(retry_after)},
        )

    text = body.text.strip()
    if not text:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"code": "empty_text", "message": "There is nothing to read out."},
        )

    try:
        result = await narration_service.synthesize(text, body.language)
    except NarrationError as exc:
        logger.warning(
            "narration_error user_id=%s code=%s status=%s chars=%s",
            user.id,
            exc.code,
            exc.status_code,
            len(text),
        )
        raise HTTPException(
            status_code=exc.status_code,
            detail={"code": exc.code, "message": exc.message},
        ) from exc

    return NarrationAudioOut(
        audio_base64=base64.b64encode(result.audio).decode("ascii"),
        mime_type=result.mime_type,
        model=result.model,
        voice=result.voice,
        language=result.language,
        cached=result.cached,
    )
