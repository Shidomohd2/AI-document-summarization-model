# Multilingual Text Summarization with mBART-50

## Overview

This project provides a multilingual text summarization pipeline using `facebook/mbart-large-50`. The system can extract text from PDFs, Word documents, PowerPoint presentations, and images, then generate concise summaries.

## Features

- Extracts text from:
  - PDFs (including embedded images)
  - Word documents (`.docx`)
  - PowerPoint slides (`.pptx`)
  - Text files (`.txt`)
  - Images (using OCR)
- Cleans and preprocesses text before summarization.
- Summarizes text using `facebook/mbart-large-50`.
- Includes error handling and logging for robustness.

## Installation

```sh
pip install -r requirements.txt
```

## Usage

### Extract and Summarize Text

```python
from utils import extract_text, summarize_text

file_path = "sample.pdf"
text = extract_text(file_path)
summary = summarize_text(text)
print(summary)
```

### File Extraction Functions

- `extract_text_from_pdf(file_path)`: Extracts text from PDFs.
- `extract_text_from_docx(file_path)`: Extracts text from Word documents.
- `extract_text_from_pptx(file_path)`: Extracts text from PowerPoint slides.
- `extract_text_from_txt(file_path)`: Extracts text from text files.
- `extract_text_from_image(image)`: Extracts text from images using OCR.

### Summarization Function

- `summarize_text(text)`: Cleans and summarizes text.


## Dependencies

- `transformers`
- `torch`
- `pytesseract`
- `PyMuPDF`
- `pdf2image`
- `Pillow`
- `python-pptx`
- `python-docx`

## Contributing

Feel free to submit issues or pull requests to enhance functionality.
