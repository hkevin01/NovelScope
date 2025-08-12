from __future__ import annotations
from pathlib import Path
from typing import Tuple
import re

def load_text(path: str | Path) -> Tuple[str, str]:
    """
    Load text from PDF or DOCX or TXT.
    Returns (text, inferred_title).
    """
    p = Path(path)
    ext = p.suffix.lower()
    if ext == ".pdf":
        text = _load_pdf(p)
    elif ext in (".docx",):
        text = _load_docx(p)
    elif ext in (".txt",):
        text = p.read_text(encoding="utf-8", errors="ignore")
    else:
        raise ValueError(f"Unsupported file type: {ext}. Use PDF, DOCX, or TXT.")
    inferred_title = _infer_title(text) or p.stem
    text = _normalize_whitespace(text)
    return text, inferred_title

def _load_pdf(p: Path) -> str:
    try:
        import fitz  # PyMuPDF
    except ImportError:
        raise RuntimeError("PyMuPDF (pymupdf) not installed. pip install pymupdf")
    text_parts = []
    with fitz.open(p) as doc:
        for page in doc:
            text_parts.append(page.get_text("text"))
    return "\n".join(text_parts)

def _load_docx(p: Path) -> str:
    try:
        import docx
    except ImportError:
        raise RuntimeError("python-docx not installed. pip install python-docx")
    doc = docx.Document(str(p))
    return "\n".join(paragraph.text for paragraph in doc.paragraphs)

def _infer_title(text: str) -> str | None:
    # Heuristic: first non-empty line in first 50 lines that is title-cased and not too long
    lines = [l.strip() for l in text.splitlines()[:50] if l.strip()]
    for line in lines:
        if 3 <= len(line.split()) <= 12 and line == line.title():
            return line
    return None

def _normalize_whitespace(s: str) -> str:
    s = s.replace("\r", "")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()
