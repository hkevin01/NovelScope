from __future__ import annotations
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from tempfile import NamedTemporaryFile
from .pipeline import analyze_file

app = FastAPI(title="NovelScope API")


@app.post("/analyze")
async def analyze_endpoint(
    file: UploadFile = File(..., description="PDF/DOCX/TXT"),
    spacy_model: str | None = Form(None),
):
    suffix = ".bin"
    if file.filename:
        if file.filename.endswith(".pdf"):
            suffix = ".pdf"
        elif file.filename.endswith(".docx"):
            suffix = ".docx"
        elif file.filename.endswith(".txt"):
            suffix = ".txt"
    with NamedTemporaryFile(delete=True, suffix=suffix) as tmp:
        content = await file.read()
        tmp.write(content)
        tmp.flush()
        meta = analyze_file(tmp.name, spacy_model=spacy_model)
        return JSONResponse(content=meta.model_dump())
