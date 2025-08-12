from __future__ import annotations
from collections import Counter, defaultdict
from typing import Dict, List
import spacy


def extract_entities(nlp, text: str, top_k: int = 15) -> Dict[str, List[str]]:
    doc = nlp(text)
    buckets = defaultdict(Counter)
    for ent in doc.ents:
        if ent.label_ in ("PERSON", "ORG", "GPE", "LOC", "NORP", "FAC", "EVENT"):
            buckets[ent.label_][ent.text] += 1
    result = {}
    for label, counter in buckets.items():
        result[label] = [t for t, _ in counter.most_common(top_k)]
    return result
