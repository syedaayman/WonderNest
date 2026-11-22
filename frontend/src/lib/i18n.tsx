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

  "home.eyebrow": "Your learning space",
  "home.greetingPrefix": "Hey",
  "home.scientist": "Scientist",
  "home.headline": "Ready for today's discoveries?",
  "home.subline": "Every big discovery begins with a curious question.",
  "home.ctaStart": "Start Learning",
  "home.ctaTutor": "Ask Your AI Tutor",
  "home.sceneLabel":
    "Illustration of a pastel science laboratory with a bubbling flask, a floating atom and molecules",
  "home.stats.completed": "lessons done",
  "home.stats.chapters": "chapters",
  "home.stats.attempts": "quiz attempts",
  "home.tutor.title": "Your science companion",
  "home.tutor.gemini": "Gemini-powered tutor",
  "home.tutor.mascotLabel": "Friendly robot science tutor mascot",
  "home.tutor.greet1": "Hello, explorer! What shall we discover today?",
  "home.tutor.greet2": "Want to understand something interesting about science?",
  "home.tutor.greet3": "Shall we try a quick science challenge?",
  "home.tutor.greet4": "Need help with today's lesson? I'm right here!",
  "home.tutor.explain": "Explain a concept",
  "home.tutor.continue": "Continue my last lesson",
  "home.tutor.quiz": "Quick quiz",
  "home.tutor.kannada": "Ask in Kannada",
  "home.tutor.diagram": "Explore a diagram",
  "home.tutor.promptExplain":
    "Explain photosynthesis in simple words with an everyday example.",
  "home.motivation.title": "Today's spark",
  "home.motivation.1": "Curiosity is the beginning of every discovery.",
  "home.motivation.2": "One new concept today. One step closer to your dreams.",
  "home.motivation.3": "Mistakes are proof that you're learning.",
  "home.motivation.4": "Scientists never stop asking why.",
  "home.goal.title": "Today's goal",
  "home.goal.minutes": "min",
  "home.goal.time": "Learning time today",
  "home.goal.completed": "lessons completed today",
  "home.goal.streak": "day streak",
  "home.goal.noStreak": "Finish a lesson to start your streak",
  "home.subjects.title": "Choose your discovery",
  "home.subjects.all": "See all chapters",
  "home.subjects.explore": "Explore",
  "home.subjects.biology.title": "Discover Living Things",
  "home.subjects.biology.body":
    "Cells, microorganisms and the human body — see how life works.",
  "home.subjects.physics.title": "Understand How Things Work",
  "home.subjects.physics.body":
    "Forces, electricity and light explained with everyday examples.",
  "home.subjects.chemistry.title": "Explore the World of Matter",
  "home.subjects.chemistry.body":
    "Particles, elements and mixtures, with colourful experiments.",
  "home.continue.title": "Continue learning",
  "home.continue.empty": "Your learning adventure starts here!",
  "home.continue.emptyBody": "Pick a chapter and your progress will appear here.",
  "home.continue.resume": "Continue",
  "home.continue.start": "Start",
  "home.cat.biology": "Biology",
  "home.cat.physics": "Physics",
  "home.cat.chemistry": "Chemistry",
  "home.cat.enrichment": "Enrichment",
  "home.fab": "Ask the tutor",
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

  "home.eyebrow": "ನಿಮ್ಮ ಕಲಿಕಾ ಜಾಗ",
  "home.greetingPrefix": "ನಮಸ್ಕಾರ",
  "home.scientist": "ವಿಜ್ಞಾನಿ",
  "home.headline": "ಇಂದಿನ ಆವಿಷ್ಕಾರಗಳಿಗೆ ಸಿದ್ಧರೇ?",
  "home.subline": "ಪ್ರತಿ ದೊಡ್ಡ ಆವಿಷ್ಕಾರವೂ ಒಂದು ಕುತೂಹಲದ ಪ್ರಶ್ನೆಯಿಂದ ಪ್ರಾರಂಭವಾಗುತ್ತದೆ.",
  "home.ctaStart": "ಕಲಿಕೆ ಪ್ರಾರಂಭಿಸಿ",
  "home.ctaTutor": "AI ಶಿಕ್ಷಕರನ್ನು ಕೇಳಿ",
  "home.sceneLabel":
    "ಬುರುಗು ಹಾಕುವ ಫ್ಲಾಸ್ಕ್, ಪರಮಾಣು ಮತ್ತು ಅಣುಗಳಿರುವ ಮೃದು ಬಣ್ಣದ ವಿಜ್ಞಾನ ಪ್ರಯೋಗಾಲಯದ ಚಿತ್ರ",
  "home.stats.completed": "ಪಾಠ ಪೂರ್ಣ",
  "home.stats.chapters": "ಅಧ್ಯಾಯಗಳು",
  "home.stats.attempts": "ರಸಪ್ರಶ್ನೆ ಪ್ರಯತ್ನ",
  "home.tutor.title": "ನಿಮ್ಮ ವಿಜ್ಞಾನ ಸಂಗಾತಿ",
  "home.tutor.gemini": "Gemini ಚಾಲಿತ ಶಿಕ್ಷಕ",
  "home.tutor.mascotLabel": "ಸ್ನೇಹಪರ ವಿಜ್ಞಾನ ಶಿಕ್ಷಕ ರೋಬೋಟ್",
  "home.tutor.greet1": "ನಮಸ್ಕಾರ, ಅನ್ವೇಷಕರೇ! ಇಂದು ಏನನ್ನು ಕಂಡುಕೊಳ್ಳೋಣ?",
  "home.tutor.greet2": "ವಿಜ್ಞಾನದ ಬಗ್ಗೆ ಒಂದು ಆಸಕ್ತಿದಾಯಕ ವಿಷಯ ತಿಳಿಯಬೇಕೇ?",
  "home.tutor.greet3": "ಒಂದು ಸಣ್ಣ ವಿಜ್ಞಾನ ಸವಾಲು ಪ್ರಯತ್ನಿಸೋಣವೇ?",
  "home.tutor.greet4": "ಇಂದಿನ ಪಾಠದಲ್ಲಿ ಸಹಾಯ ಬೇಕೇ? ನಾನು ಇಲ್ಲಿದ್ದೇನೆ!",
  "home.tutor.explain": "ಒಂದು ಪರಿಕಲ್ಪನೆ ವಿವರಿಸಿ",
  "home.tutor.continue": "ಕೊನೆಯ ಪಾಠ ಮುಂದುವರಿಸಿ",
  "home.tutor.quiz": "ಸಣ್ಣ ರಸಪ್ರಶ್ನೆ",
  "home.tutor.kannada": "ಕನ್ನಡದಲ್ಲಿ ಕೇಳಿ",
  "home.tutor.diagram": "ಚಿತ್ರ ಅನ್ವೇಷಿಸಿ",
  "home.tutor.promptExplain":
    "ದ್ಯುತಿಸಂಶ್ಲೇಷಣೆಯನ್ನು ಸರಳವಾಗಿ, ದಿನನಿತ್ಯದ ಉದಾಹರಣೆಯೊಂದಿಗೆ ವಿವರಿಸಿ.",
  "home.motivation.title": "ಇಂದಿನ ಕಿಡಿ",
  "home.motivation.1": "ಕುತೂಹಲವೇ ಪ್ರತಿ ಆವಿಷ್ಕಾರದ ಆರಂಭ.",
  "home.motivation.2": "ಇಂದು ಒಂದು ಹೊಸ ಪರಿಕಲ್ಪನೆ. ನಿಮ್ಮ ಕನಸಿನತ್ತ ಒಂದು ಹೆಜ್ಜೆ.",
  "home.motivation.3": "ತಪ್ಪುಗಳೇ ನೀವು ಕಲಿಯುತ್ತಿದ್ದೀರಿ ಎಂಬುದರ ಸಾಕ್ಷಿ.",
  "home.motivation.4": "ವಿಜ್ಞಾನಿಗಳು ಎಂದಿಗೂ 'ಏಕೆ' ಎಂದು ಕೇಳುವುದನ್ನು ನಿಲ್ಲಿಸುವುದಿಲ್ಲ.",
  "home.goal.title": "ಇಂದಿನ ಗುರಿ",
  "home.goal.minutes": "ನಿಮಿಷ",
  "home.goal.time": "ಇಂದು ಕಲಿಕೆಯ ಸಮಯ",
  "home.goal.completed": "ಪಾಠ ಇಂದು ಪೂರ್ಣ",
  "home.goal.streak": "ದಿನಗಳ ಸರಣಿ",
  "home.goal.noStreak": "ಸರಣಿ ಆರಂಭಿಸಲು ಒಂದು ಪಾಠ ಮುಗಿಸಿ",
  "home.subjects.title": "ನಿಮ್ಮ ಆವಿಷ್ಕಾರ ಆಯ್ಕೆಮಾಡಿ",
  "home.subjects.all": "ಎಲ್ಲಾ ಅಧ್ಯಾಯಗಳು",
  "home.subjects.explore": "ಅನ್ವೇಷಿಸಿ",
  "home.subjects.biology.title": "ಜೀವಿಗಳನ್ನು ಅನ್ವೇಷಿಸಿ",
  "home.subjects.biology.body":
    "ಜೀವಕೋಶಗಳು, ಸೂಕ್ಷ್ಮಜೀವಿಗಳು ಮತ್ತು ಮಾನವ ದೇಹ — ಜೀವನ ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ ಎಂದು ತಿಳಿಯಿರಿ.",
  "home.subjects.physics.title": "ವಸ್ತುಗಳು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತವೆ",
  "home.subjects.physics.body":
    "ಬಲ, ವಿದ್ಯುತ್ ಮತ್ತು ಬೆಳಕು — ದಿನನಿತ್ಯದ ಉದಾಹರಣೆಗಳೊಂದಿಗೆ ವಿವರಣೆ.",
  "home.subjects.chemistry.title": "ವಸ್ತುವಿನ ಜಗತ್ತನ್ನು ಅನ್ವೇಷಿಸಿ",
  "home.subjects.chemistry.body":
    "ಕಣಗಳು, ಮೂಲಧಾತುಗಳು ಮತ್ತು ಮಿಶ್ರಣಗಳು — ಬಣ್ಣದ ಪ್ರಯೋಗಗಳೊಂದಿಗೆ.",
  "home.continue.title": "ಕಲಿಕೆ ಮುಂದುವರಿಸಿ",
  "home.continue.empty": "ನಿಮ್ಮ ಕಲಿಕಾ ಸಾಹಸ ಇಲ್ಲಿಂದ ಪ್ರಾರಂಭವಾಗುತ್ತದೆ!",
  "home.continue.emptyBody": "ಒಂದು ಅಧ್ಯಾಯ ಆಯ್ಕೆಮಾಡಿ — ನಿಮ್ಮ ಪ್ರಗತಿ ಇಲ್ಲಿ ಕಾಣಿಸುತ್ತದೆ.",
  "home.continue.resume": "ಮುಂದುವರಿಸಿ",
  "home.continue.start": "ಪ್ರಾರಂಭಿಸಿ",
  "home.cat.biology": "ಜೀವಶಾಸ್ತ್ರ",
  "home.cat.physics": "ಭೌತಶಾಸ್ತ್ರ",
  "home.cat.chemistry": "ರಸಾಯನಶಾಸ್ತ್ರ",
  "home.cat.enrichment": "ಪೂರಕ",
  "home.fab": "ಶಿಕ್ಷಕರನ್ನು ಕೇಳಿ",
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
