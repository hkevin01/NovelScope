from __future__ import annotations
from typing import Dict
import textstat


def compute_readability(text: str) -> Dict[str, float]:
    return {
        "flesch_reading_ease": float(textstat.flesch_reading_ease(text)),
        "flesch_kincaid_grade": float(textstat.flesch_kincaid_grade(text)),
        "coleman_liau_index": float(textstat.coleman_liau_index(text)),
        "smog_index": float(textstat.smog_index(text)),
        "automated_readability_index": float(textstat.automated_readability_index(text)),
        "dale_chall_readability_score": float(textstat.dale_chall_readability_score(text)),
    }
