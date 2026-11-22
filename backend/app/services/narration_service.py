"""Diagram narration: turn a short explanation into spoken audio.

The narration text always comes from the backend's own diagram copy, never from the browser,
so a student cannot use this endpoint as a free text-to-speech service for arbitrary content.

Gemini TTS is used when the configured API key can actually reach a TTS model. Model names
change over time, so the service *discovers* TTS models from the provider instead of trusting a
hard-coded name: if the project has no TTS model the endpoint reports that honestly and the
client falls back to the device voice. Nothing here ever returns silence pretending to be audio.
"""

from __future__ import annotations

import asyncio
import hashlib
import io
import logging
import threading
import time
import wave
from dataclasses import dataclass

from google import genai
from google.genai import types

from app.core.config import get_settings

logger = logging.getLogger("wondernest.narration")

# Gemini TTS returns raw little-endian 16-bit PCM at 24 kHz, mono. Browsers need a container.
PCM_SAMPLE_RATE = 24_000
PCM_SAMPLE_WIDTH = 2
PCM_CHANNELS = 1

CACHE_MAX_ENTRIES = 96
DISCOVERY_TTL_SECONDS = 900


class NarrationError(Exception):
    """Base error carrying the HTTP status and a machine readable code."""

    code = "narration_error"
    status_code = 502
    message = "Narration is not available right now."

    def __init__(self, message: str | None = None, *, detail: str | None = None) -> None:
        super().__init__(message or self.message)
        self.message = message or self.message
        self.detail = detail


class NarrationNotConfiguredError(NarrationError):
    code = "ai_not_configured"
    status_code = 503
    message = "Narration needs a Gemini API key on the server."


class NarrationUnavailableError(NarrationError):
    code = "tts_unavailable"
    status_code = 503
    message = "This Gemini project does not expose a text-to-speech model."


class NarrationRateLimitedError(NarrationError):
    code = "tts_rate_limited"
    status_code = 429
    message = "Too many narration requests. Please wait a moment."


class NarrationProviderError(NarrationError):
    code = "tts_provider_error"
    status_code = 502
    message = "The speech service did not answer. Please try again."


@dataclass(frozen=True)
class NarrationAudio:
    audio: bytes
    mime_type: str
    model: str
    voice: str | None
    language: str
    cached: bool


@dataclass(frozen=True)
class NarrationStatus:
    available: bool
    model: str | None
    reason: str | None
    detail: str | None


_lock = threading.Lock()
_cache: "dict[str, tuple[bytes, str, str, str | None, str]]" = {}
_cache_order: list[str] = []
_discovery: "tuple[float, list[str]] | None" = None
_discovery_lock = threading.Lock()


def _client() -> genai.Client:
    settings = get_settings()
    if not settings.GEMINI_API_KEY:
        raise NarrationNotConfiguredError()
    return genai.Client(api_key=settings.GEMINI_API_KEY)


def _voice_for(language: str) -> str:
    settings = get_settings()
    if language == "kn":
        return settings.GEMINI_TTS_VOICE_KN or "Kore"
    return settings.GEMINI_TTS_VOICE_EN or "Puck"


def _cache_key(text: str, language: str, voice: str) -> str:
    digest = hashlib.sha256(f"{language}|{voice}|{text}".encode("utf-8")).hexdigest()
    return digest


def _remember(key: str, value: tuple[bytes, str, str, str | None, str]) -> None:
    with _lock:
        _cache[key] = value
        _cache_order.append(key)
        while len(_cache_order) > CACHE_MAX_ENTRIES:
            oldest = _cache_order.pop(0)
            _cache.pop(oldest, None)


def clear_cache() -> None:
    """Drop cached audio. Used by tests so a cache hit never masks a provider change."""
    global _discovery
    with _lock:
        _cache.clear()
        _cache_order.clear()
    with _discovery_lock:
        _discovery = None


def _discover_tts_models(client: genai.Client) -> list[str]:
    """Return the TTS model names this key can use, cached briefly.

    A project may expose no TTS model at all; that is a configuration fact, not an error, so
    the caller decides what to tell the student.
    """
    global _discovery
    now = time.monotonic()
    with _discovery_lock:
        if _discovery is not None and now - _discovery[0] < DISCOVERY_TTL_SECONDS:
            return _discovery[1]

    names: list[str] = []
    try:
        for model in client.models.list():
            name = getattr(model, "name", "") or ""
            if "tts" in name.lower() and "image" not in name.lower():
                names.append(name.split("/", 1)[-1])
    except Exception as exc:  # noqa: BLE001 - any provider failure means "cannot confirm"
        logger.warning("tts_model_discovery_failed error=%s", type(exc).__name__)
        names = []

    with _discovery_lock:
        _discovery = (now, names)
    return names


def _pcm_to_wav(pcm: bytes) -> bytes:
    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as handle:
        handle.setnchannels(PCM_CHANNELS)
        handle.setsampwidth(PCM_SAMPLE_WIDTH)
        handle.setframerate(PCM_SAMPLE_RATE)
        handle.writeframes(pcm)
    return buffer.getvalue()


def _call_tts(client: genai.Client, model: str, text: str, voice: str) -> tuple[bytes, str]:
    """Synchronous provider call, run in a worker thread by :func:`synthesize`."""
    speech_config = types.SpeechConfig(
        voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=voice)
        )
    )
    try:
        response = client.models.generate_content(
            model=model,
            contents=text,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=speech_config,
            ),
        )
    except Exception as exc:  # noqa: BLE001
        message = str(exc)
        # Some API revisions reject the voice selection field while still supporting audio.
        if "speechConfig" in message or "speech_config" in message:
            response = client.models.generate_content(
                model=model,
                contents=text,
                config=types.GenerateContentConfig(response_modalities=["AUDIO"]),
            )
        else:
            raise

    candidates = getattr(response, "candidates", None) or []
    for candidate in candidates:
        content = getattr(candidate, "content", None)
        for part in getattr(content, "parts", None) or []:
            inline = getattr(part, "inline_data", None)
            data = getattr(inline, "data", None)
            if data:
                mime = getattr(inline, "mime_type", "") or ""
                if "wav" in mime.lower():
                    return bytes(data), "audio/wav"
                return _pcm_to_wav(bytes(data)), "audio/wav"
    raise NarrationProviderError(
        "The speech service returned no audio.", detail="empty_audio_response"
    )


def _translate(exc: Exception) -> NarrationError:
    text = str(exc)
    lowered = text.lower()
    if "api key" in lowered or "permission" in lowered or "401" in text or "403" in text:
        return NarrationProviderError(
            "The speech service rejected the server's credentials.",
            detail="invalid_key",
        )
    if "429" in text or "quota" in lowered or "rate" in lowered:
        return NarrationRateLimitedError()
    if "404" in text or "not found" in lowered or "not supported" in lowered:
        return NarrationUnavailableError()
    return NarrationProviderError(detail=type(exc).__name__)


async def synthesize(text: str, language: str) -> NarrationAudio:
    """Return spoken audio for ``text``, reusing cached audio for repeated explanations."""
    settings = get_settings()
    if not settings.GEMINI_API_KEY:
        raise NarrationNotConfiguredError()

    language = language if language in {"kn", "en"} else "en"
    voice = _voice_for(language)
    key = _cache_key(text, language, voice)

    with _lock:
        hit = _cache.get(key)
    if hit is not None:
        audio, mime, model, cached_voice, cached_language = hit
        return NarrationAudio(
            audio=audio,
            mime_type=mime,
            model=model,
            voice=cached_voice,
            language=cached_language,
            cached=True,
        )

    client = _client()
    models = await asyncio.to_thread(_discover_tts_models, client)
    preferred = (settings.GEMINI_TTS_MODEL or "").strip()
    ordered = [preferred] + [name for name in models if name != preferred]
    ordered = [name for name in ordered if name]
    if not ordered:
        raise NarrationUnavailableError(
            "No Gemini text-to-speech model is available for this API key.",
            detail="no_tts_model",
        )

    last_error: NarrationError | None = None
    for model in ordered:
        try:
            audio, mime = await asyncio.wait_for(
                asyncio.to_thread(_call_tts, client, model, text, voice),
                timeout=settings.GEMINI_TTS_TIMEOUT_SECONDS,
            )
        except asyncio.TimeoutError:
            last_error = NarrationProviderError(
                "The speech service took too long.", detail="timeout"
            )
            continue
        except NarrationError as exc:
            last_error = exc
            continue
        except Exception as exc:  # noqa: BLE001
            last_error = _translate(exc)
            continue

        _remember(key, (audio, mime, model, voice, language))
        logger.info(
            "narration_synthesised model=%s lang=%s chars=%s bytes=%s",
            model,
            language,
            len(text),
            len(audio),
        )
        return NarrationAudio(
            audio=audio,
            mime_type=mime,
            model=model,
            voice=voice,
            language=language,
            cached=False,
        )

    raise last_error or NarrationUnavailableError()


async def status() -> NarrationStatus:
    """Report whether real speech generation is possible, without generating anything."""
    settings = get_settings()
    if not settings.GEMINI_API_KEY:
        return NarrationStatus(
            available=False,
            model=None,
            reason="not_configured",
            detail="No Gemini API key is set on the server.",
        )
    try:
        models = await asyncio.to_thread(_discover_tts_models, _client())
    except NarrationError as exc:
        return NarrationStatus(
            available=False, model=None, reason="provider_error", detail=exc.message
        )
    except Exception as exc:  # noqa: BLE001
        return NarrationStatus(
            available=False, model=None, reason="provider_error", detail=type(exc).__name__
        )

    if not models:
        return NarrationStatus(
            available=False,
            model=None,
            reason="no_tts_model",
            detail="This Gemini project exposes no text-to-speech model.",
        )
    preferred = (settings.GEMINI_TTS_MODEL or "").strip()
    model = preferred if preferred in models else models[0]
    return NarrationStatus(available=True, model=model, reason=None, detail=None)
