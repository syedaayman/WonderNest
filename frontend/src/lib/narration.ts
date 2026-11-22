/**
 * Diagram narration engine.
 *
 * One narration plays at a time across the whole app, so a student clicking around a diagram
 * never gets two voices talking together. The backend is asked first because it holds the
 * Gemini key; when the project's key has no text-to-speech model (or the provider fails) the
 * engine falls back to the device voice in `kn-IN` / `en-IN` and says so in the UI instead of
 * pretending Gemini spoke. The written explanation is always shown regardless of audio.
 */

import { useEffect, useState } from "react";

import { api, ApiError } from "./api";
import type { Lang } from "./i18n";

export type NarrationStatus = "idle" | "loading" | "playing" | "paused";
export type NarrationSource = "gemini" | "device" | null;

export interface NarrationSnapshot {
  status: NarrationStatus;
  source: NarrationSource;
  enabled: boolean;
  error: string | null;
  text: string | null;
  language: Lang | null;
  /** null until the backend status is known. */
  geminiAvailable: boolean | null;
  geminiModel: string | null;
  geminiReason: string | null;
}

const MUTED_KEY = "wondernest.narration.muted";

const listeners = new Set<() => void>();

let snapshot: NarrationSnapshot = {
  status: "idle",
  source: null,
  enabled: localStorage.getItem(MUTED_KEY) !== "1",
  error: null,
  text: null,
  language: null,
  geminiAvailable: null,
  geminiModel: null,
  geminiReason: null,
};

function update(patch: Partial<NarrationSnapshot>): void {
  snapshot = { ...snapshot, ...patch };
  for (const listener of listeners) listener();
}

export function getNarration(): NarrationSnapshot {
  return snapshot;
}

function subscribe(listener: () => void): () => void {
  listeners.add(listener);
  return () => {
    listeners.delete(listener);
  };
}

// --- audio handles ----------------------------------------------------------------

let audio: HTMLAudioElement | null = null;
let objectUrl: string | null = null;
let utterance: SpeechSynthesisUtterance | null = null;

function releaseAudio(): void {
  if (audio) {
    audio.onended = null;
    audio.onerror = null;
    audio.pause();
    audio = null;
  }
  if (objectUrl) {
    URL.revokeObjectURL(objectUrl);
    objectUrl = null;
  }
}

function releaseDevice(): void {
  if (typeof window !== "undefined" && window.speechSynthesis) {
    window.speechSynthesis.cancel();
  }
  utterance = null;
}

function stopEverything(): void {
  releaseAudio();
  releaseDevice();
}

// --- backend capability -----------------------------------------------------------

let statusPromise: Promise<void> | null = null;

/** Asks the backend once per session whether it can really synthesise speech. */
export function ensureNarrationStatus(): Promise<void> {
  if (statusPromise) return statusPromise;
  statusPromise = (async () => {
    try {
      const result = await api.narrationStatus();
      update({
        geminiAvailable: result.available,
        geminiModel: result.model,
        geminiReason: result.reason,
      });
    } catch {
      // Unknown is not the same as unavailable: leave it null and let speak() try the backend.
      statusPromise = null;
    }
  })();
  return statusPromise;
}

// --- device voice -----------------------------------------------------------------

function pickVoice(synth: SpeechSynthesis, lang: string): SpeechSynthesisVoice | null {
  const voices = synth.getVoices();
  if (!voices.length) return null;
  const wanted = lang.toLowerCase();
  const exact = voices.find((voice) => voice.lang.toLowerCase() === wanted);
  if (exact) return exact;
  const prefix = wanted.slice(0, 2);
  const sameLanguage = voices.find((voice) => voice.lang.toLowerCase().startsWith(prefix));
  return sameLanguage ?? null;
}

function deviceSpeak(text: string, lang: Lang): void {
  const synth = typeof window === "undefined" ? null : window.speechSynthesis;
  if (!synth) {
    update({
      status: "idle",
      source: null,
      error: "This browser cannot speak text aloud. The explanation is written above.",
    });
    return;
  }

  const speakNow = () => {
    const utter = new SpeechSynthesisUtterance(text);
    utter.lang = lang === "kn" ? "kn-IN" : "en-IN";
    utter.rate = 0.94;
    utter.pitch = 1;
    const voice = pickVoice(synth, utter.lang);
    if (voice) utter.voice = voice;
    utter.onend = () => update({ status: "idle" });
    utter.onerror = () => update({ status: "idle" });
    utterance = utter;
    update({ status: "playing", source: "device", error: null });
    synth.speak(utter);
  };

  // Chrome populates the voice list asynchronously; give it one tick before giving up.
  if (!synth.getVoices().length) {
    let settled = false;
    const onChange = () => {
      if (settled) return;
      settled = true;
      synth.onvoiceschanged = null;
      speakNow();
    };
    synth.onvoiceschanged = onChange;
    window.setTimeout(() => {
      if (!settled) {
        settled = true;
        synth.onvoiceschanged = null;
        speakNow();
      }
    }, 400);
    return;
  }

  speakNow();
}

// --- public controls --------------------------------------------------------------

function playBase64(base64: string, mimeType: string): void {
  const binary = atob(base64);
  const bytes = new Uint8Array(binary.length);
  for (let index = 0; index < binary.length; index += 1) {
    bytes[index] = binary.charCodeAt(index);
  }
  const blob = new Blob([bytes], { type: mimeType || "audio/wav" });
  objectUrl = URL.createObjectURL(blob);
  const element = new Audio(objectUrl);
  audio = element;
  element.onended = () => {
    releaseAudio();
    update({ status: "idle" });
  };
  element.onerror = () => {
    releaseAudio();
    update({ status: "idle", error: "The audio could not be played." });
  };
  update({ status: "playing", source: "gemini", error: null });
  void element.play().catch(() => {
    releaseAudio();
    update({
      status: "idle",
      error: "Your browser blocked audio playback. Tap the listen button again.",
    });
  });
}

/** Speaks one explanation. Returns once playback has started (or has fallen back). */
export async function narrate(text: string, lang: Lang): Promise<void> {
  const clean = text.trim();
  if (!clean) return;

  stopEverything();

  if (!snapshot.enabled) {
    // Muted: the caller still shows the written explanation.
    update({ status: "idle", source: null, text: clean, language: lang });
    return;
  }

  update({ status: "loading", error: null, text: clean, language: lang, source: null });

  if (snapshot.geminiAvailable !== false) {
    try {
      const result = await api.narrationSpeak(clean, lang);
      update({ geminiAvailable: true, geminiModel: result.model });
      playBase64(result.audio_base64, result.mime_type);
      return;
    } catch (error) {
      if (error instanceof ApiError && error.code === "tts_unavailable") {
        update({ geminiAvailable: false, geminiReason: "no_tts_model" });
      } else if (error instanceof ApiError && error.status === 429) {
        update({ error: error.message });
      }
      // Fall through to the device voice rather than leaving the student with silence.
    }
  }

  deviceSpeak(clean, lang);
}

export function pauseNarration(): void {
  if (snapshot.status !== "playing") return;
  if (audio) {
    audio.pause();
    update({ status: "paused" });
    return;
  }
  if (utterance && typeof window !== "undefined" && window.speechSynthesis) {
    window.speechSynthesis.pause();
    update({ status: "paused" });
  }
}

export function resumeNarration(): void {
  if (snapshot.status !== "paused") return;
  if (audio) {
    void audio.play().catch(() => undefined);
    update({ status: "playing" });
    return;
  }
  if (utterance && typeof window !== "undefined" && window.speechSynthesis) {
    window.speechSynthesis.resume();
    update({ status: "playing" });
  }
}

export function stopNarration(): void {
  stopEverything();
  update({ status: "idle" });
}

export function replayNarration(): void {
  const { text, language } = snapshot;
  if (!text || !language) return;
  void narrate(text, language);
}

export function setNarrationEnabled(enabled: boolean): void {
  localStorage.setItem(MUTED_KEY, enabled ? "0" : "1");
  if (!enabled) stopEverything();
  update({ enabled, status: enabled ? snapshot.status : "idle" });
}

/** React binding: re-renders the caller whenever narration state changes. */
export function useNarration() {
  const [state, setState] = useState<NarrationSnapshot>(snapshot);

  useEffect(() => {
    const unsubscribe = subscribe(() => setState(snapshot));
    void ensureNarrationStatus();
    return unsubscribe;
  }, []);

  return {
    ...state,
    narrate,
    pause: pauseNarration,
    resume: resumeNarration,
    stop: stopNarration,
    replay: replayNarration,
    setEnabled: setNarrationEnabled,
  };
}
