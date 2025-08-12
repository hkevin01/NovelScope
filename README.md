# NovelScope

**Advanced Novel Analysis Tool** - Extract deep insights from your novels with comprehensive NLP analysis.

NovelScope is a powerful Python tool that analyzes novels in PDF, DOCX, and TXT formats. It automatically segments texts into chapters and extracts rich metadata including readability metrics, sentiment analysis, named entities, keywords, dialogue ratios, and chapter summaries.

## ✨ Features

### 📖 Document Processing

- **Multi-format Support**: PDF, DOCX, and TXT files
- **Intelligent Chapter Detection**: Automatic segmentation with regex patterns
- **Fallback Handling**: Smart processing for unstructured texts

### 🧠 NLP Analysis Pipeline

- **Readability Metrics**: Flesch Reading Ease, Flesch-Kincaid Grade, Coleman-Liau Index, SMOG, and more
- **Sentiment Analysis**: Chapter-level sentiment scoring using VADER
- **Named Entity Recognition**: Person, location, and organization extraction with spaCy
- **Keyword Extraction**: Automatic keyword identification using YAKE algorithm
- **Text Summarization**: Chapter summaries using TextRank algorithm
- **Dialogue Analysis**: Dialogue detection and ratio calculation

### 🖥️ Interfaces

- **Command Line Interface**: Easy-to-use CLI with rich output formatting
- **REST API**: FastAPI web server for programmatic access
- **Structured Output**: JSON format with comprehensive metadata

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/hkevin01/NovelScope.git
cd NovelScope

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .

# Download required models
python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download('punkt'); nltk.download('vader_lexicon')"
```

### Basic Usage

```bash
# Analyze a novel
novelscope analyze path/to/your/novel.pdf --out results/

# Start API server
novelscope api
```

## 📚 Usage Examples

### Command Line Interface

```bash
# Analyze a PDF novel
novelscope analyze data/input/novel.pdf --out data/output/

# Analyze a DOCX file
novelscope analyze manuscript.docx --out analysis/

# Analyze a text file
novelscope analyze story.txt --out results/
```

### API Usage

Start the server:
```bash
novelscope api
```

Upload and analyze via curl:

```bash
curl -X POST "http://localhost:8000/analyze" \
     -F "file=@novel.pdf"
```

### Python API

```python
from novelscope.pipeline import analyze_file

# Analyze a file programmatically
metadata = analyze_file("path/to/novel.pdf")
print(f"Found {len(metadata.chapters)} chapters")
print(f"Total words: {metadata.word_count}")
```

## 📊 Output Format

NovelScope generates comprehensive JSON output with the following structure:

```json
{
  "title": "Novel Title",
  "author": null,
  "language": "en",
  "word_count": 50000,
  "sentence_count": 2500,
  "chapters": [
    {
      "index": 0,
      "title": "Chapter 1: The Beginning",
      "start_char": 0,
      "end_char": 2500,
      "text": "Chapter content...",
      "word_count": 1200,
      "sentence_count": 60,
      "avg_sentence_length": 20.0,
      "dialogue_ratio": 0.25,
      "readability": {
        "flesch_reading_ease": 65.5,
        "flesch_kincaid_grade": 8.2,
        "coleman_liau_index": 7.8,
        "smog_index": 9.1
      },
      "sentiment": {
        "compound": 0.15,
        "positive": 0.6,
        "neutral": 0.3,
        "negative": 0.1
      },
      "entities": [
        {"text": "Alice", "label": "PERSON", "count": 15},
        {"text": "London", "label": "GPE", "count": 8}
      ],
      "keywords": [
        {"keyword": "mystery", "score": 0.85},
        {"keyword": "investigation", "score": 0.72}
      ],
      "summary": "Chapter summary using TextRank..."
    }
  ]
}
```

## 🛠️ Development

### Project Structure

```text
NovelScope/
├── src/novelscope/           # Main package
│   ├── __init__.py
│   ├── cli.py               # Command line interface
│   ├── server.py            # FastAPI web server
│   ├── pipeline.py          # Main analysis pipeline
│   ├── models.py            # Pydantic data models
│   ├── ingestion.py         # File parsing (PDF/DOCX/TXT)
│   ├── segmentation.py      # Chapter detection
│   └── analyzers/           # NLP analysis modules
│       ├── readability.py
│       ├── sentiment.py
│       ├── entities.py
│       ├── keywords.py
│       ├── summary.py
│       └── dialogue.py
├── tests/                   # Unit tests
├── data/                    # Sample data and outputs
├── pyproject.toml          # Project configuration
└── README.md
```

### Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test
python -m pytest tests/test_segmentation.py -v

# Run with coverage
python -m pytest tests/ --cov=novelscope
```

### Dependencies

**Core Dependencies:**

- `spacy>=3.7.0` - NLP processing and NER
- `pydantic>=2.6.0` - Data validation and models
- `typer>=0.9.0` - CLI framework
- `fastapi>=0.104.0` - Web API framework
- `rich>=13.0.0` - Terminal formatting

**Document Processing:**

- `pymupdf>=1.21.0` - PDF processing
- `python-docx>=0.8.11` - DOCX processing
- `pdfminer.six>=20221105` - Alternative PDF processing

**NLP & Analysis:**

- `nltk>=3.8.1` - Natural language toolkit
- `textstat>=0.7.3` - Readability metrics
- `yake>=0.4.8` - Keyword extraction
- `sumy>=0.11.0` - Text summarization

## 🗺️ Roadmap

### Near Term

- [ ] Character relationship graphs with coreference resolution
- [ ] Topic modeling integration (BERTopic/KeyBERT)
- [ ] Export formats (CSV, Excel, HTML reports)
- [ ] Batch processing capabilities

### Future Plans

- [ ] LLM-powered literary criticism (OpenAI/Ollama integration)
- [ ] Interactive web dashboard
- [ ] Custom model training for genre-specific analysis
- [ ] Multi-language support expansion
- [ ] Integration with popular writing tools

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [spaCy](https://spacy.io/) for excellent NLP capabilities
- [NLTK](https://www.nltk.org/) for foundational NLP tools
- [YAKE](https://github.com/LIAAD/yake) for keyword extraction
- [TextRank](https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf) algorithm for summarization

## 📞 Support

If you encounter any issues or have questions:

- Open an issue on GitHub
- Check the documentation in the `docs/` directory
- Review existing issues for similar problems

---

**NovelScope** - Unlock the secrets hidden in your stories! 📚✨
