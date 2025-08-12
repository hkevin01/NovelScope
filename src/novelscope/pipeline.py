from __future__ import annotations
from typing import Dict, List
from .models import ChapterMetadata, NovelMetadata
from .ingestion import load_text
from .segmentation import split_into_chapters
from .nlp import load_spacy
from .utils.text import count_words, count_sentences
from .analyzers.entities import extract_entities
from .analyzers.keywords import extract_keywords
from .analyzers.readability import compute_readability
from .analyzers.dialogue import dialogue_ratio
from .analyzers.sentiment import sentiment_scores
from .analyzers.summary import summarize


def analyze_file(path: str, spacy_model: str | None = None) -> NovelMetadata:
    text, inferred_title = load_text(path)
    nlp = load_spacy(spacy_model)

    chaps_raw = split_into_chapters(text)
    chapters: List[ChapterMetadata] = []

    for idx, (chap_text, start, end, title) in enumerate(chaps_raw):
        wc = count_words(chap_text)
        sc = count_sentences(chap_text)
        avg_len = round(wc / sc, 2) if sc else float(wc)
        dia = dialogue_ratio(chap_text)
        read = compute_readability(chap_text)
        ents = extract_entities(nlp, chap_text, top_k=15)
        keys = extract_keywords(chap_text, top_k=12)
        sent = sentiment_scores(chap_text)
        summ = summarize(chap_text, sentences=5)

        chapters.append(ChapterMetadata(
            index=idx,
            title=title,
            start_char=start,
            end_char=end,
            text=chap_text,
            word_count=wc,
            sentence_count=sc,
            avg_sentence_length=avg_len,
            dialogue_ratio=dia,
            readability=read,
            entities=ents,
            keywords=keys,
            sentiment=sent,
            summary=summ
        ))

    # Aggregate top entities across chapters
    agg: Dict[str, Dict[str, int]] = {}
    for ch in chapters:
        for label, items in ch.entities.items():
            agg.setdefault(label, {})
            for it in items:
                agg[label][it] = agg[label].get(it, 0) + 1

    top_entities = {lbl: [k for k, _ in sorted(cnt.items(), key=lambda x: x[1], reverse=True)[:20]]
                    for lbl, cnt in agg.items()}

    total_words = sum(c.word_count for c in chapters)
    total_sents = sum(c.sentence_count for c in chapters)

    return NovelMetadata(
        title=inferred_title,
        author=None,
        language="en",
        word_count=total_words,
        sentence_count=total_sents,
        chapters=chapters,
        top_entities=top_entities,
    )
