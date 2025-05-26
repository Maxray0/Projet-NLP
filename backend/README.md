# Projet-NLP

## Description
This project uses FastAPI to create an API for processing and translating text from PDF and image files. It leverages Hugging Face's transformers for language detection and translation.

## Installation
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd Projet-NLP
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r backend/requirements.txt
    ```

## Usage
1. Run the FastAPI server:
    ```bash
    uvicorn backend.api:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

## Endpoints
- `POST /traduction`: Upload a PDF or image file and specify the target language for translation. The API will return the original text, detected language, and translated text.

## Example
To process a file, use the following `curl` command:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/process/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@<path-to-your-file>' \
  -F 'target_lang=en'
```
## ques ce c'est
pytesseract.pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.