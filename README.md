# NovelScope

Analyze novels (PDF/DOCX): split into chapters, extract metadata, tags, sentiment, readability, and summaries. Outputs JSON and CSV.

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download('vader_lexicon')"

novelscope analyze data/input/example.pdf --out data/output
```

## Features

- PDF/DOCX ingest (PyMuPDF, python-docx)
- Chapter segmentation
- NER, keywords, readability, sentiment, dialogue ratio, summaries
- CLI and API server

## Roadmap

- Character graphs, coref (BookNLP)
- Topic modeling (BERTopic/KeyBERT)
- LLM critique (OpenAI/Ollama)

## License

MIT
