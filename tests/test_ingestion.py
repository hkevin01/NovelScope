from pathlib import Path
from novelscope.ingestion import load_text


def test_txt_ingest(tmp_path: Path):
    p = tmp_path / "a.txt"
    p.write_text("Title\n\nChapter 1\nHello world.")
    text, title = load_text(str(p))
    assert "Hello world" in text
    assert title in ("Title", "a")
