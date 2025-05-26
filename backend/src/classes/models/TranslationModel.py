from backend.src.classes.enums.LanguagesEnum import LANGUAGE_MAP, LanguagesEnum
from backend.src.classes.models.BaseHFModel import BaseHFModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

TASK = "translation_XX_to_YY"
MODEL_NAME = "facebook/nllb-200-distilled-600M"

class TranslationModel(BaseHFModel):
    
    def __init__(self):
        super().__init__(TASK, AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME), AutoTokenizer.from_pretrained(MODEL_NAME))
        
    def predict(self, inputs, src_lang: LanguagesEnum, tgt_lang: LanguagesEnum):
        return self.model(inputs, src_lang=src_lang.nllb, tgt_lang=tgt_lang.nllb)[0]['translation_text']