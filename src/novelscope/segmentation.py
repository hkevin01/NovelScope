from __future__ import annotations
import re
from typing import List, Tuple

CHAPTER_RE = re.compile(
    r"^\s*(chapter|chap\.|capitulo|kapitel)\s+([ivxlcdm\d]+)\b.*$",
    re.IGNORECASE | re.MULTILINE
)

ALT_CHAPTER_RE = re.compile(
    r"^\s*(?:chapter\s*)?(\d+)\s*$",
    re.IGNORECASE | re.MULTILINE
)


def split_into_chapters(text: str) -> List[Tuple[str, int, int, str | None]]:
    """
    Returns a list of tuples: (chapter_text, start_char, end_char, title)
    If no chapters detected, returns one "chapter" (the whole text).
    """
    matches = list(CHAPTER_RE.finditer(text))
    if not matches:
        # Check for alternative chapter numbering patterns
        alt = list(ALT_CHAPTER_RE.finditer(text))
        if alt:
            return _cut_by_anchors(text, alt)
        else:
            # For short texts or no chapter markers, return as single chapter
            if len(text) < 10000:  # Threshold for short texts
                return [(text.strip(), 0, len(text), None)]
            else:
                # For very long texts without chapters, split into chunks
                anchors = _equidistant_anchors(text, parts=10)
                return _cut_by_anchors(text, anchors)

    anchors = [(m.start(), m.group(0).strip()) for m in matches]
    chapters = []
    for i, (start, heading) in enumerate(anchors):
        end = anchors[i+1][0] if i+1 < len(anchors) else len(text)
        chapter_text = text[start:end].strip()
        chapters.append((chapter_text, start, end, heading))
    return chapters


def _equidistant_anchors(text: str, parts: int):
    size = len(text)
    anchors = []
    for i in range(0, parts):
        pos = int(i * size / parts)
        anchors.append(_FakeMatch(pos))
    return anchors


def _cut_by_anchors(text: str, anchors):
    chapters = []
    for i, m in enumerate(anchors):
        start = m.start()
        end = anchors[i+1].start() if i+1 < len(anchors) else len(text)
        chapter_text = text[start:end].strip()
        title = getattr(m, "group", lambda x=None: None)()
        if title:
            title = title.strip()
        chapters.append((chapter_text, start, end, title))
    return chapters


class _FakeMatch:
    def __init__(self, start_pos: int):
        self._start = start_pos
        
    def start(self):
        return self._start
