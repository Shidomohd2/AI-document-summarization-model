# Multilingual Text Summarization with mBART-50

## Overview

This project provides a multilingual text summarization pipeline using `facebook/mbart-large-50`. The system can extract text from PDFs, Word documents, PowerPoint presentations, and images, then generate concise summaries. The summarization functionality is integrated into a Django web application and is used within `views.py` to provide document-based chatbot interactions.

## Features

- Extracts text from:
  - PDFs (including embedded images)
  - Word documents (`.docx`)
  - PowerPoint slides (`.pptx`)
  - Text files (`.txt`)
  - Images (using OCR)
- Cleans and preprocesses text before summarization.
- Summarizes text using `facebook/mbart-large-50`.
- Django-based chat interface that allows users to upload documents and request summaries by page number.
- Stores chat sessions and messages in the database.

## Installation

```sh
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Usage

### Using the Chat Interface
1. Upload a document via the web interface.
2. The system extracts pages and asks which page to summarize.
3. Enter a page number to receive the summary.

### API Endpoints
- `POST /chat/` - Upload a document or request a summary by page number.
- `GET /chat/history/` - Retrieve chat history.

### Extract and Summarize Text in Django Views

```python
from .utils import process_file, extract_pages

file_path = "sample.pdf"
pages = extract_pages(file_path)
summary = process_file(pages[0])  # Summarize first page
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

## File Structure


## Dependencies

- `Django`
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

