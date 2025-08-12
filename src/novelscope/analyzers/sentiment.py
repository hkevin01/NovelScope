from __future__ import annotations
from typing import Dict
from nltk.sentiment import SentimentIntensityAnalyzer

_sia = None


def _get_sia():
    global _sia
    if _sia is None:
        _sia = SentimentIntensityAnalyzer()
    return _sia


def sentiment_scores(text: str) -> Dict[str, float]:
    sia = _get_sia()
    scores = sia.polarity_scores(text)
    # scores: {'neg': x, 'neu': y, 'pos': z, 'compound': c}
    return {k: float(v) for k, v in scores.items()}
