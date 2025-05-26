from backend.src.classes.Predictions import TranslationPrediction
from backend.src.classes.enums.LanguagesEnum import LANGUAGE_MAP, LanguageUtils, LanguagesEnum
from backend.src.classes.models.LanguageDetectionModel import LanguageDetectionModel
from backend.src.classes.models.TranslationModel import TranslationModel
from backend.src.classes.utils.extractUtils import extract_text
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

LANGUAGE_CLASSIFIER = LanguageDetectionModel()
TRANSLATION_NLP = TranslationModel()

@app.post("/translate")
async def process_file(file: UploadFile = File(...), target_lang: LanguagesEnum = LanguagesEnum.FRANCE):
    text = await extract_text(file)

    language = LANGUAGE_CLASSIFIER.predict(text)
    translated = TRANSLATION_NLP.predict(text, language, LANGUAGE_MAP[target_lang])

    return TranslationPrediction.create(language, text, translated)

@app.get("/languages")
async def get_languages():
    return LanguageUtils.values()

@app.post("/cv-classifier")
async def process_file(files: list[UploadFile] = [File(...)], target_lang: LanguagesEnum = LanguagesEnum.FRANCE):
    text = await extract_text(files)