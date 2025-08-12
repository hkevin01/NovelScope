from __future__ import annotations
import re


def count_words(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))


def count_sentences(text: str) -> int:
    # simple heuristic; spaCy provides better counts, but this is fast
    return max(1, len(re.findall(r"[.!?]+(?:\s|$)", text)))
