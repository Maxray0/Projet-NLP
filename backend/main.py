from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Détection langue
from transformers import pipeline as hf_pipeline
lang_detect = hf_pipeline("text-classification", model="papluca/xlm-roberta-base-language-detection")

# Traduction
model_name = "facebook/nllb-200-distilled-600M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

translation_pipeline = pipeline("translation", model=model, tokenizer=tokenizer)

def extract_text_from_pdf(file_bytes):
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_image(file_bytes):
    image = Image.open(io.BytesIO(file_bytes))
    return pytesseract.image_to_string(image)

@app.post("/traduction")
async def process_file(file: UploadFile = File(...), target_lang: str = "eng_Latn"):
    file_bytes = await file.read()

    if file.content_type == "application/pdf":
        text = extract_text_from_pdf(file_bytes)
    else:
        text = extract_text_from_image(file_bytes)

    text_sample = text[:400]
    detected_lang = lang_detect(text_sample)[0]["label"]

    # Traduction si nécessaire
    translated_text = translation_pipeline(
        text_sample,
        src_lang=detected_lang,
        tgt_lang=target_lang
    )[0]['translation_text']

    return {
        "detected_language": detected_lang,
        "original_text": text,
        "translated_text": translated_text
    }

@app.get("/languages")
async def get_languages():
    ISO_TO_NLLB = {
        "fr": "fra_Latn",
        "en": "eng_Latn",
        "es": "spa_Latn",
        "ar": "arb_Arab",
        "de": "deu_Latn",
        "pt": "por_Latn",
        "it": "ita_Latn",
        "ja": "jpn_Jpan",
        "ko": "kor_Hang",
        "pl": "pol_Latn",
        "sv": "swe_Latn",
        "cs": "ces_Latn",
        "uk": "ukr_Cyrl",
        "vi": "vie_Latn",
    }
    return ISO_TO_NLLB
