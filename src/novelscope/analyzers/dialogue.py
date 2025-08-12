from __future__ import annotations


def dialogue_ratio(text: str) -> float:
    """
    Approximate dialogue by proportion of characters inside quotes.
    """
    total = max(len(text), 1)
    in_quotes = 0
    i = 0
    quote = False
    for ch in text:
        if ch in ['"', '"', '"', '«', '»', "'"]:
            quote = not quote
        if quote:
            in_quotes += 1
        i += 1
    return round(in_quotes / total, 4)
