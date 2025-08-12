from __future__ import annotations
from typing import List
import yake


def extract_keywords(text: str, top_k: int = 15) -> List[str]:
    kw_extractor = yake.KeywordExtractor(lan="en", n=3, top=top_k, dedupLim=0.9)
    keywords = kw_extractor.extract_keywords(text)
    # returns list of (key, score); lower score = better
    return [k for k, _ in sorted(keywords, key=lambda x: x[1])]
