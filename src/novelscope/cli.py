from __future__ import annotations
from pathlib import Path
import json
import typer
from rich import print as rprint
from .pipeline import analyze_file

app = typer.Typer(help="NovelScope CLI")


@app.command()
def analyze(
    file: str = typer.Argument(..., help="Path to PDF/DOCX/TXT"),
    out: str = typer.Option("data/output", help="Output folder"),
    model: str = typer.Option(None, help="spaCy model name (e.g., en_core_web_sm or en_core_web_trf)"),
    save_text: bool = typer.Option(False, help="Save chapter texts to files"),
):
    """Analyze a novel and store JSON outputs."""
    Path(out).mkdir(parents=True, exist_ok=True)
    rprint(f"[bold cyan]Analyzing[/] {file} ...")
    meta = analyze_file(file, spacy_model=model)

    # Write overall JSON
    overall_path = Path(out) / "novel.json"
    with overall_path.open("w", encoding="utf-8") as f:
        json.dump(meta.model_dump(), f, ensure_ascii=False, indent=2)
    rprint(f"[green]Wrote[/] {overall_path}")

    # Write per-chapter JSON
    chapters_dir = Path(out) / "chapters"
    chapters_dir.mkdir(exist_ok=True)
    for ch in meta.chapters:
        ch_path = chapters_dir / f"chapter_{ch.index:03d}.json"
        with ch_path.open("w", encoding="utf-8") as f:
            json.dump(ch.model_dump(), f, ensure_ascii=False, indent=2)
        if save_text:
            txt_path = chapters_dir / f"chapter_{ch.index:03d}.txt"
            txt_path.write_text(ch.text, encoding="utf-8")

    rprint(f"[bold green]Done.[/] Chapters: {len(meta.chapters)}")


@app.command()
def api(
    host: str = typer.Option("127.0.0.1", help="Host"),
    port: int = typer.Option(8000, help="Port"),
    workers: int = typer.Option(1, help="Uvicorn workers"),
):
    """Run API server for file uploads."""
    import uvicorn
    uvicorn.run("novelscope.server:app", host=host, port=port, reload=False, workers=workers)
