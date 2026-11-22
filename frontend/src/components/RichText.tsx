import { Fragment, type ReactNode } from "react";

/** Renders **bold** spans inside a line of tutor text. */
function inline(text: string): ReactNode[] {
  const parts = text.split(/(\*\*[^*]+\*\*)/g).filter(Boolean);
  return parts.map((part, index) => {
    if (part.startsWith("**") && part.endsWith("**")) {
      return <strong key={index}>{part.slice(2, -2)}</strong>;
    }
    return <Fragment key={index}>{part}</Fragment>;
  });
}

/**
 * Small, dependency-free renderer for the tutor's Markdown-ish replies.
 * Supports paragraphs, "-" / "•" bullets, numbered lists and "**bold**" text.
 * React escapes the content, so model output can never inject HTML.
 */
export function RichText({ text }: { text: string }) {
  const lines = text.replace(/\r\n/g, "\n").split("\n");
  const blocks: ReactNode[] = [];
  let bullets: string[] = [];

  const flushBullets = () => {
    if (!bullets.length) return;
    blocks.push(
      <ul key={`ul-${blocks.length}`}>
        {bullets.map((item, index) => (
          <li key={index}>{inline(item)}</li>
        ))}
      </ul>,
    );
    bullets = [];
  };

  lines.forEach((rawLine, index) => {
    const line = rawLine.trim();
    if (!line) {
      flushBullets();
      return;
    }

    const bulletMatch = line.match(/^(?:[-*•]|\d+[.)])\s+(.*)$/);
    if (bulletMatch) {
      bullets.push(bulletMatch[1]);
      return;
    }

    flushBullets();

    const headingMatch = line.match(/^#{1,6}\s+(.*)$/);
    if (headingMatch) {
      blocks.push(<h3 key={`h-${index}`}>{inline(headingMatch[1])}</h3>);
      return;
    }

    blocks.push(<p key={`p-${index}`}>{inline(line)}</p>);
  });

  flushBullets();
  return <>{blocks}</>;
}
