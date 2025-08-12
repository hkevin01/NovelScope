from __future__ import annotations
from typing import List, Dict, Optional
from pydantic import BaseModel, Field

class ChapterMetadata(BaseModel):
    index: int
    title: Optional[str] = None
    start_char: int
    end_char: int
    text: str
    word_count: int
    sentence_count: int
    avg_sentence_length: float
    dialogue_ratio: float
    readability: Dict[str, float] = Field(default_factory=dict)
    entities: Dict[str, List[str]] = Field(default_factory=dict)  # PER, LOC, ORG, etc.
    keywords: List[str] = Field(default_factory=list)
    sentiment: Dict[str, float] = Field(default_factory=dict)  # compound/pos/neg/neu
    summary: Optional[str] = None

class NovelMetadata(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    language: Optional[str] = "en"
    word_count: int
    sentence_count: int
    chapters: List[ChapterMetadata]
    top_entities: Dict[str, List[str]] = Field(default_factory=dict)
