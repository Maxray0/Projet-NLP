from backend.src.classes.enums.LanguagesEnum import LanguageUtils
from backend.src.classes.models.BaseHFModel import BaseHFModel

TASK = "text-classification"
MODEL_NAME = "papluca/xlm-roberta-base-language-detection"

class LanguageDetectionModel(BaseHFModel):
    
    def __init__(self):
        super().__init__(TASK, MODEL_NAME)
        
    def predict(self, inputs):
        return LanguageUtils.find_by_iso((super().predict(inputs))[0]["label"])