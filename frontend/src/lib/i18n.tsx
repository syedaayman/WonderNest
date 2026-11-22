/**
 * Global English / ಕನ್ನಡ language state.
 *
 * The choice is stored in localStorage so it survives navigation and reloads, and every page
 * reads content in the selected language. Scientific terms stay in both languages where the
 * curriculum stores them, so a student never loses the English name of a concept.
 */

import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useState,
  type ReactNode,
} from "react";

export type Lang = "kn" | "en";

const STORAGE_KEY = "wondernest.language";

type Dict = Record<string, string>;

const EN: Dict = {
  "nav.dashboard": "Dashboard",
  "nav.curriculum": "Curriculum",
  "nav.tutor": "AI Tutor",
  "nav.progress": "Progress",
  "nav.logout": "Log out",
  "common.loading": "Loading…",
  "common.retry": "Try again",
  "common.back": "Back",
  "common.copy": "Copy",
  "common.copied": "Copied ✓",
  "common.clear": "Clear",
  "common.close": "Close",
  "common.minutes": "min",
  "common.chapters": "chapters",
  "common.questions": "questions",
  "common.language": "Language",
  "curriculum.eyebrow": "Curriculum",
  "curriculum.title": "Class 8 Science",
  "curriculum.subtitle":
    "Karnataka State Board · Curiosity · seven learning units plus two enrichment topics.",
  "curriculum.enrichment": "Enrichment",
  "curriculum.enrichmentNote":
    "Extra topics for curious minds — not textbook units, but great for understanding diagrams.",
  "curriculum.start": "Start learning",
  "curriculum.continue": "Continue",
  "curriculum.review": "Review",
  "curriculum.quiz": "Practice quiz",
  "curriculum.progress": "Progress",
  "curriculum.notStarted": "Not started",
  "curriculum.bestScore": "Best score",
  "curriculum.objectives": "learning objectives",
  "curriculum.empty": "No chapters yet. Seed the curriculum from the backend to see units here.",
  "chapter.tab.learn": "Learn",
  "chapter.tab.visualize": "Visualize",
  "chapter.tab.notes": "Notes",
  "chapter.tab.videos": "Videos",
  "chapter.tab.quiz": "Practice Quiz",
  "chapter.tab.tutor": "Ask AI Tutor",
  "chapter.objectives": "What you will learn",
  "chapter.example": "Everyday example",
  "chapter.keyTerms": "Key terms",
  "chapter.notesTitle": "Quick revision notes",
  "chapter.notesHint": "Short points to read the night before a test.",
  "chapter.print": "Print notes",
  "chapter.videosTitle": "Watch and learn",
  "chapter.videosHint":
    "Verified Kannada and English channels. Links open on YouTube — nothing autoplays here.",
  "chapter.searchOnYoutube": "Search on YouTube",
  "chapter.quizTitle": "Chapter practice quiz",
  "chapter.quizHint": "Five questions from this chapter only.",
  "chapter.startQuiz": "Start the quiz",
  "chapter.tutorTitle": "Ask the tutor about this chapter",
  "chapter.tutorHint":
    "The tutor already knows this chapter, its topics and your language choice.",
  "chapter.openTutor": "Open the AI tutor",
  "chapter.visualizeTitle": "Explore the diagram",
  "chapter.visualizeHint": "Tap the labels and controls to see how the science works.",
  "chapter.sourceNote": "Study material note",
  "quiz.eyebrow": "Practice quiz",
  "quiz.answered": "answered",
  "quiz.submit": "Submit answers",
  "quiz.checking": "Checking…",
  "quiz.allAnswered": "All questions answered — ready to submit.",
  "quiz.someUnanswered": "unanswered questions will be marked wrong.",
  "quiz.hint": "Need a hint? Ask the tutor",
  "quiz.loading": "Loading quiz…",
  "quiz.level": "Level",
  "results.eyebrow": "Quiz result",
  "results.review": "Review",
  "results.correct": "Correct",
  "results.needsPractice": "Needs practice",
  "results.yourAnswer": "Your answer",
  "results.correctAnswer": "Correct answer",
  "results.notAnswered": "Not answered",
  "results.tryAgain": "Try again",
  "results.progress": "View progress",
  "results.askTutor": "✦ Ask the tutor to explain",
  "results.explanation": "Why",
  "tutor.title": "WonderNest AI Tutor",
  "tutor.poweredBy": "Powered by Google Gemini",
  "tutor.online": "AI online",
  "tutor.offline": "AI not configured",
  "tutor.clear": "Clear conversation",
  "tutor.level": "Level",
  "tutor.context": "Chapter context",
  "tutor.emptyTitle": "Ask me anything about Class 8 Science.",
  "tutor.emptyBody":
    "I explain concepts in Kannada or English, use everyday examples, give hints for quiz questions and ask you questions back. I am an AI study helper — not an official textbook.",
  "tutor.placeholderKn": "ನಿಮ್ಮ ಪ್ರಶ್ನೆಯನ್ನು ಇಲ್ಲಿ ಬರೆಯಿರಿ… (ಉದಾ: ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆ ಎಂದರೇನು?)",
  "tutor.placeholderEn": "Ask your question here… (e.g. What is friction?)",
  "tutor.send": "Ask tutor",
  "tutor.sending": "Thinking…",
  "tutor.thinking": "Tutor is thinking",
  "tutor.micStart": "Ask by voice",
  "tutor.micStop": "Stop recording",
  "tutor.micCancel": "Cancel",
  "tutor.micRecording": "Listening… speak your question",
  "tutor.micTranscribing": "Writing down what you said…",
  "tutor.micHint": "Voice questions need a quiet room and microphone permission.",
  "tutor.micDenied":
    "Microphone access was blocked. Allow the microphone in your browser settings, or type your question instead.",
  "tutor.micUnsupported":
    "This browser cannot record audio. Please type your question — the tutor still answers in Kannada or English.",
  "tutor.micEmpty": "I could not hear a question. Try again a little closer to the microphone.",
  "tutor.footnote":
    "Responses are generated by Google Gemini for learning support. They are not official Karnataka State Board material — always check your textbook.",
  "tutor.browse": "Browse curriculum",
  "tutor.rateLimit": "questions",
  "tutor.slowDown": "Slow down a little.",
  "tutor.errorTitle": "Tutor error",
};

const KN: Dict = {
  "nav.dashboard": "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್",
  "nav.curriculum": "ಪಠ್ಯಕ್ರಮ",
  "nav.tutor": "AI ಶಿಕ್ಷಕ",
  "nav.progress": "ಪ್ರಗತಿ",
  "nav.logout": "ಲಾಗ್ ಔಟ್",
  "common.loading": "ಲೋಡ್ ಆಗುತ್ತಿದೆ…",
  "common.retry": "ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ",
  "common.back": "ಹಿಂದೆ",
  "common.copy": "ನಕಲಿಸಿ",
  "common.copied": "ನಕಲಾಗಿದೆ ✓",
  "common.clear": "ಅಳಿಸಿ",
  "common.close": "ಮುಚ್ಚಿ",
  "common.minutes": "ನಿಮಿಷ",
  "common.chapters": "ಘಟಕಗಳು",
  "common.questions": "ಪ್ರಶ್ನೆಗಳು",
  "common.language": "ಭಾಷೆ",
  "curriculum.eyebrow": "ಪಠ್ಯಕ್ರಮ",
  "curriculum.title": "8ನೇ ತರಗತಿ ವಿಜ್ಞಾನ",
  "curriculum.subtitle":
    "ಕರ್ನಾಟಕ ರಾಜ್ಯ ಮಂಡಳಿ · ಕ್ಯೂರಿಯಾಸಿಟಿ · ಏಳು ಕಲಿಕಾ ಘಟಕಗಳು ಮತ್ತು ಎರಡು ಹೆಚ್ಚುವರಿ ವಿಷಯಗಳು.",
  "curriculum.enrichment": "ಹೆಚ್ಚುವರಿ",
  "curriculum.enrichmentNote":
    "ಕುತೂಹಲವಿರುವ ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ ಹೆಚ್ಚುವರಿ ವಿಷಯಗಳು — ಪಠ್ಯಪುಸ್ತಕದ ಘಟಕಗಳಲ್ಲ, ಆದರೆ ಚಿತ್ರಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಸಹಾಯಕ.",
  "curriculum.start": "ಕಲಿಕೆ ಪ್ರಾರಂಭಿಸಿ",
  "curriculum.continue": "ಮುಂದುವರಿಸಿ",
  "curriculum.review": "ಪುನರಾವರ್ತನೆ",
  "curriculum.quiz": "ಅಭ್ಯಾಸ ರಸಪ್ರಶ್ನೆ",
  "curriculum.progress": "ಪ್ರಗತಿ",
  "curriculum.notStarted": "ಪ್ರಾರಂಭವಾಗಿಲ್ಲ",
  "curriculum.bestScore": "ಅತ್ಯುತ್ತಮ ಅಂಕ",
  "curriculum.objectives": "ಕಲಿಕಾ ಗುರಿಗಳು",
  "curriculum.empty":
    "ಇನ್ನೂ ಘಟಕಗಳಿಲ್ಲ. ಬ್ಯಾಕೆಂಡ್‌ನಿಂದ ಪಠ್ಯಕ್ರಮವನ್ನು ಸೇರಿಸಿ.",
  "chapter.tab.learn": "ಕಲಿಯಿರಿ",
  "chapter.tab.visualize": "ಚಿತ್ರಗಳು",
  "chapter.tab.notes": "ಟಿಪ್ಪಣಿಗಳು",
  "chapter.tab.videos": "ವೀಡಿಯೊಗಳು",
  "chapter.tab.quiz": "ಅಭ್ಯಾಸ ರಸಪ್ರಶ್ನೆ",
  "chapter.tab.tutor": "AI ಶಿಕ್ಷಕರನ್ನು ಕೇಳಿ",
  "chapter.objectives": "ನೀವು ಕಲಿಯುವ ವಿಷಯಗಳು",
  "chapter.example": "ದೈನಂದಿನ ಉದಾಹರಣೆ",
  "chapter.keyTerms": "ಮುಖ್ಯ ಪದಗಳು",
  "chapter.notesTitle": "ತ್ವರಿತ ಪುನರಾವರ್ತನೆ ಟಿಪ್ಪಣಿಗಳು",
  "chapter.notesHint": "ಪರೀಕ್ಷೆಯ ಹಿಂದಿನ ರಾತ್ರಿ ಓದಲು ಸಣ್ಣ ಅಂಶಗಳು.",
  "chapter.print": "ಟಿಪ್ಪಣಿಗಳನ್ನು ಮುದ್ರಿಸಿ",
  "chapter.videosTitle": "ನೋಡಿ ಕಲಿಯಿರಿ",
  "chapter.videosHint":
    "ಕನ್ನಡ ಮತ್ತು ಇಂಗ್ಲಿಷ್ ಶಿಕ್ಷಣ ಚಾನೆಲ್‌ಗಳು. ಕೊಂಡಿಗಳು YouTube ನಲ್ಲಿ ತೆರೆಯುತ್ತವೆ — ಇಲ್ಲಿ ಯಾವುದೂ ತಾನಾಗಿ ಚಲಿಸುವುದಿಲ್ಲ.",
  "chapter.searchOnYoutube": "YouTube ನಲ್ಲಿ ಹುಡುಕಿ",
  "chapter.quizTitle": "ಘಟಕದ ಅಭ್ಯಾಸ ರಸಪ್ರಶ್ನೆ",
  "chapter.quizHint": "ಈ ಘಟಕದ ಐದು ಪ್ರಶ್ನೆಗಳು ಮಾತ್ರ.",
  "chapter.startQuiz": "ರಸಪ್ರಶ್ನೆ ಪ್ರಾರಂಭಿಸಿ",
  "chapter.tutorTitle": "ಈ ಘಟಕದ ಬಗ್ಗೆ ಶಿಕ್ಷಕರನ್ನು ಕೇಳಿ",
  "chapter.tutorHint":
    "ಶಿಕ್ಷಕರಿಗೆ ಈ ಘಟಕ, ವಿಷಯಗಳು ಮತ್ತು ನಿಮ್ಮ ಭಾಷೆ ಈಗಾಗಲೇ ತಿಳಿದಿದೆ.",
  "chapter.openTutor": "AI ಶಿಕ್ಷಕರನ್ನು ತೆರೆಯಿರಿ",
  "chapter.visualizeTitle": "ಚಿತ್ರವನ್ನು ಅನ್ವೇಷಿಸಿ",
  "chapter.visualizeHint": "ವಿಜ್ಞಾನ ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ ಎಂದು ನೋಡಲು ಗುರುತುಗಳನ್ನು ಒತ್ತಿರಿ.",
  "chapter.sourceNote": "ಅಧ್ಯಯನ ಸಾಮಗ್ರಿ ಟಿಪ್ಪಣಿ",
  "quiz.eyebrow": "ಅಭ್ಯಾಸ ರಸಪ್ರಶ್ನೆ",
  "quiz.answered": "ಉತ್ತರಿಸಲಾಗಿದೆ",
  "quiz.submit": "ಉತ್ತರಗಳನ್ನು ಸಲ್ಲಿಸಿ",
  "quiz.checking": "ಪರಿಶೀಲಿಸುತ್ತಿದೆ…",
  "quiz.allAnswered": "ಎಲ್ಲಾ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸಿದ್ದೀರಿ — ಸಲ್ಲಿಸಲು ಸಿದ್ಧ.",
  "quiz.someUnanswered": "ಉತ್ತರಿಸದ ಪ್ರಶ್ನೆಗಳು ತಪ್ಪು ಎಂದು ಪರಿಗಣಿಸಲಾಗುತ್ತದೆ.",
  "quiz.hint": "ಸುಳಿವು ಬೇಕೇ? ಶಿಕ್ಷಕರನ್ನು ಕೇಳಿ",
  "quiz.loading": "ರಸಪ್ರಶ್ನೆ ಲೋಡ್ ಆಗುತ್ತಿದೆ…",
  "quiz.level": "ಮಟ್ಟ",
  "results.eyebrow": "ರಸಪ್ರಶ್ನೆ ಫಲಿತಾಂಶ",
  "results.review": "ಪುನರ್ವಿಮರ್ಶೆ",
  "results.correct": "ಸರಿ",
  "results.needsPractice": "ಅಭ್ಯಾಸ ಬೇಕು",
  "results.yourAnswer": "ನಿಮ್ಮ ಉತ್ತರ",
  "results.correctAnswer": "ಸರಿಯಾದ ಉತ್ತರ",
  "results.notAnswered": "ಉತ್ತರಿಸಿಲ್ಲ",
  "results.tryAgain": "ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ",
  "results.progress": "ಪ್ರಗತಿ ನೋಡಿ",
  "results.askTutor": "✦ ಶಿಕ್ಷಕರಿಂದ ವಿವರಣೆ ಪಡೆಯಿರಿ",
  "results.explanation": "ಏಕೆ",
  "tutor.title": "WonderNest AI ಶಿಕ್ಷಕ",
  "tutor.poweredBy": "Google Gemini ನಿಂದ ಚಾಲಿತ",
  "tutor.online": "AI ಸಿದ್ಧವಾಗಿದೆ",
  "tutor.offline": "AI ಸಂರಚಿಸಲಾಗಿಲ್ಲ",
  "tutor.clear": "ಸಂಭಾಷಣೆ ಅಳಿಸಿ",
  "tutor.level": "ಮಟ್ಟ",
  "tutor.context": "ಘಟಕದ ಸಂದರ್ಭ",
  "tutor.emptyTitle": "8ನೇ ತರಗತಿ ವಿಜ್ಞಾನದ ಯಾವುದೇ ಪ್ರಶ್ನೆ ಕೇಳಿ.",
  "tutor.emptyBody":
    "ನಾನು ಕನ್ನಡ ಅಥವಾ ಇಂಗ್ಲಿಷ್‌ನಲ್ಲಿ ವಿವರಿಸುತ್ತೇನೆ, ದೈನಂದಿನ ಉದಾಹರಣೆಗಳನ್ನು ಬಳಸುತ್ತೇನೆ, ರಸಪ್ರಶ್ನೆಗೆ ಸುಳಿವು ಕೊಡುತ್ತೇನೆ ಮತ್ತು ನಿಮಗೆ ಪ್ರಶ್ನೆಗಳನ್ನು ಕೇಳುತ್ತೇನೆ. ನಾನು AI ಅಧ್ಯಯನ ಸಹಾಯಕ — ಅಧಿಕೃತ ಪಠ್ಯಪುಸ್ತಕವಲ್ಲ.",
  "tutor.placeholderKn": "ನಿಮ್ಮ ಪ್ರಶ್ನೆಯನ್ನು ಇಲ್ಲಿ ಬರೆಯಿರಿ… (ಉದಾ: ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆ ಎಂದರೇನು?)",
  "tutor.placeholderEn": "Ask your question here… (e.g. What is friction?)",
  "tutor.send": "ಶಿಕ್ಷಕರನ್ನು ಕೇಳಿ",
  "tutor.sending": "ಯೋಚಿಸುತ್ತಿದೆ…",
  "tutor.thinking": "ಶಿಕ್ಷಕರು ಯೋಚಿಸುತ್ತಿದ್ದಾರೆ",
  "tutor.micStart": "ಧ್ವನಿಯಲ್ಲಿ ಕೇಳಿ",
  "tutor.micStop": "ರೆಕಾರ್ಡಿಂಗ್ ನಿಲ್ಲಿಸಿ",
  "tutor.micCancel": "ರದ್ದುಮಾಡಿ",
  "tutor.micRecording": "ಕೇಳುತ್ತಿದ್ದೇನೆ… ನಿಮ್ಮ ಪ್ರಶ್ನೆ ಹೇಳಿ",
  "tutor.micTranscribing": "ನೀವು ಹೇಳಿದ್ದನ್ನು ಬರೆಯುತ್ತಿದ್ದೇನೆ…",
  "tutor.micHint": "ಧ್ವನಿ ಪ್ರಶ್ನೆಗಳಿಗೆ ಶಾಂತ ಕೋಣೆ ಮತ್ತು ಮೈಕ್ರೊಫೋನ್ ಅನುಮತಿ ಬೇಕು.",
  "tutor.micDenied":
    "ಮೈಕ್ರೊಫೋನ್ ಅನುಮತಿ ನಿರಾಕರಿಸಲಾಗಿದೆ. ಬ್ರೌಸರ್ ಸೆಟ್ಟಿಂಗ್‌ನಲ್ಲಿ ಅನುಮತಿ ಕೊಡಿ, ಅಥವಾ ಪ್ರಶ್ನೆಯನ್ನು ಟೈಪ್ ಮಾಡಿ.",
  "tutor.micUnsupported":
    "ಈ ಬ್ರೌಸರ್ ಧ್ವನಿ ರೆಕಾರ್ಡ್ ಮಾಡಲಾರದು. ದಯವಿಟ್ಟು ಟೈಪ್ ಮಾಡಿ — ಶಿಕ್ಷಕರು ಕನ್ನಡ ಅಥವಾ ಇಂಗ್ಲಿಷ್‌ನಲ್ಲಿ ಉತ್ತರಿಸುತ್ತಾರೆ.",
  "tutor.micEmpty": "ಪ್ರಶ್ನೆ ಕೇಳಿಸಲಿಲ್ಲ. ಮೈಕ್ರೊಫೋನ್ ಹತ್ತಿರ ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ.",
  "tutor.footnote":
    "ಉತ್ತರಗಳನ್ನು Google Gemini ಕಲಿಕಾ ಸಹಾಯಕ್ಕಾಗಿ ರಚಿಸುತ್ತದೆ. ಇವು ಅಧಿಕೃತ ಕರ್ನಾಟಕ ರಾಜ್ಯ ಮಂಡಳಿ ಸಾಮಗ್ರಿಯಲ್ಲ — ಪಠ್ಯಪುಸ್ತಕವನ್ನು ಪರಿಶೀಲಿಸಿ.",
  "tutor.browse": "ಪಠ್ಯಕ್ರಮ ನೋಡಿ",
  "tutor.rateLimit": "ಪ್ರಶ್ನೆಗಳು",
  "tutor.slowDown": "ಸ್ವಲ್ಪ ನಿಧಾನವಾಗಿ.",
  "tutor.errorTitle": "ಶಿಕ್ಷಕರ ದೋಷ",
};

const DICTS: Record<Lang, Dict> = { en: EN, kn: KN };

interface LanguageState {
  lang: Lang;
  setLang: (next: Lang) => void;
  toggle: () => void;
  t: (key: string) => string;
}

const LanguageContext = createContext<LanguageState | null>(null);

function storedLanguage(): Lang {
  const raw = localStorage.getItem(STORAGE_KEY);
  return raw === "en" || raw === "kn" ? raw : "kn";
}

export function LanguageProvider({ children }: { children: ReactNode }) {
  const [lang, setLangState] = useState<Lang>(storedLanguage);

  useEffect(() => {
    localStorage.setItem(STORAGE_KEY, lang);
    document.documentElement.lang = lang === "kn" ? "kn" : "en";
  }, [lang]);

  const setLang = useCallback((next: Lang) => setLangState(next), []);
  const toggle = useCallback(() => setLangState((cur) => (cur === "kn" ? "en" : "kn")), []);

  const t = useCallback(
    (key: string) => DICTS[lang][key] ?? DICTS.en[key] ?? key,
    [lang],
  );

  const value = useMemo(() => ({ lang, setLang, toggle, t }), [lang, setLang, toggle, t]);

  return <LanguageContext.Provider value={value}>{children}</LanguageContext.Provider>;
}

export function useLanguage(): LanguageState {
  const context = useContext(LanguageContext);
  if (!context) throw new Error("useLanguage must be used inside LanguageProvider");
  return context;
}

/** Picks the Kannada or English variant of stored content, falling back to whichever exists. */
export function pick(lang: Lang, en: string | null | undefined, kn: string | null | undefined): string {
  const primary = lang === "kn" ? kn : en;
  const fallback = lang === "kn" ? en : kn;
  return (primary ?? fallback ?? "").trim();
}
