from backend.src.classes.enums.LanguagesEnum import LanguagesEnum
from pydantic import BaseModel

class TranslationPrediction(BaseModel):
    detected_language: LanguagesEnum = None
    original_text: str = None
    translated_text: str = None
    
    @staticmethod
    def create(detected_language, original_text, translated_text):
        this = TranslationPrediction()
        this.detected_language = detected_language
        this.original_text = original_text
        this.translated_text = translated_text
        return this