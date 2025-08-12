from __future__ import annotations
from typing import Optional
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer


def summarize(text: str, sentences: int = 5) -> Optional[str]:
    text = text.strip()
    if not text:
        return None
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    sents = summarizer(parser.document, sentences)
    return " ".join(str(s) for s in sents)
