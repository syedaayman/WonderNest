"""Schemas for voice input transcription."""

from pydantic import BaseModel, Field


class TranscribeRequest(BaseModel):
    """A short browser recording, base64 encoded so no extra upload dependency is needed."""

    audio_base64: str = Field(min_length=16, max_length=12_000_000)
    mime_type: str = Field(default="audio/webm", max_length=100)
    language: str = Field(default="en", pattern="^(en|kn)$")


class TranscribeResponse(BaseModel):
    text: str
    model: str
