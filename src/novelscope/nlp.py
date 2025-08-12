from __future__ import annotations
from typing import Optional
import spacy


def load_spacy(model: Optional[str] = None):
    """
    Load spaCy model; default to en_core_web_sm.
    You can pass en_core_web_trf for better accuracy (requires transformers/torch).
    """
    name = model or "en_core_web_sm"
    try:
        nlp = spacy.load(name)
    except OSError:
        raise RuntimeError(f"spaCy model '{name}' not installed. Try: python -m spacy download {name}")
    return nlp
