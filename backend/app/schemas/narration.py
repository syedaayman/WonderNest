"""Schemas for diagram narration (text-to-speech)."""

from typing import Literal

from pydantic import BaseModel, Field


class NarrationRequest(BaseModel):
    """A diagram explanation to speak. ``text`` is bounded so the endpoint stays cheap."""

    text: str = Field(min_length=1, max_length=900)
    language: Literal["kn", "en"] = "en"


class NarrationAudioOut(BaseModel):
    audio_base64: str
    mime_type: str
    model: str
    voice: str | None = None
    language: str
    cached: bool


class NarrationStatusOut(BaseModel):
    """Whether the server can generate real speech right now.

    ``reason`` is one of ``not_configured``, ``no_tts_model`` or ``provider_error``; the client
    uses it to explain the situation and to fall back to the device voice.
    """

    available: bool
    model: str | None = None
    reason: str | None = None
    detail: str | None = None
