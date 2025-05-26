
from enum import Enum
from pydantic import BaseModel

class Languages(BaseModel):
    label: str
    iso: str
    nllb: str
    
    class Config:
        frozen = True

class LanguagesEnum(str, Enum):
    FRANCE = "FRANCE"
    ENGLISH = "ENGLISH"
    ESPANOL = "ESPANOL"
    ARABE = "ARABE"
    ALLEMAND = "ALLEMAND"
    PORTUGAIS = "PORTUGAIS"
    ITALIEN = "ITALIEN"
    JAPONAIS = "JAPONAIS"
    COREEN = "COREEN"
    POLONAIS = "POLONAIS"
    SUEDOIS = "SUEDOIS"
    TCHEQUE = "TCHEQUE"
    UKRAINIEN = "UKRAINIEN"
    VIETNAMIEN = "VIETNAMIEN"
    
LANGUAGE_MAP = {
    LanguagesEnum.FRANCE: Languages(**{'label': "Francais", 'iso': "fr", 'nllb': "fra_Latn"}),
    LanguagesEnum.ENGLISH: Languages(**{'label': "English", 'iso': "en", 'nllb': "eng_Latn"}),
    LanguagesEnum.ESPANOL: Languages(**{'label': "Español", 'iso': "es", 'nllb': "spa_Latn"}),
    LanguagesEnum.ARABE: Languages(**{'label': "العربية", 'iso': "ar", 'nllb': "arb_Arab"}),
    LanguagesEnum.ALLEMAND: Languages(**{'label': "Deutsch", 'iso': "de", 'nllb': "deu_Latn"}),
    LanguagesEnum.PORTUGAIS: Languages(**{'label': "Português", 'iso': "pt", 'nllb': "por_Latn"}),
    LanguagesEnum.ITALIEN: Languages(**{'label': "Italiano", 'iso': "it", 'nllb': "ita_Latn"}),
    LanguagesEnum.JAPONAIS: Languages(**{'label': "日本語", 'iso': "ja", 'nllb': "jpn_Jpan"}),
    LanguagesEnum.COREEN: Languages(**{'label': "한국어", 'iso': "ko", 'nllb': "kor_Hang"}),
    LanguagesEnum.POLONAIS: Languages(**{'label': "Polski", 'iso': "pl", 'nllb': "pol_Latn"}),
    LanguagesEnum.SUEDOIS: Languages(**{'label': "Svenska", 'iso': "sv", 'nllb': "swe_Latn"}),
    LanguagesEnum.TCHEQUE: Languages(**{'label': "Čeština", 'iso': "cs", 'nllb': "ces_Latn"}),
    LanguagesEnum.UKRAINIEN: Languages(**{'label': "Українська", 'iso': "uk", 'nllb': "ukr_Cyrl"}),
    LanguagesEnum.VIETNAMIEN: Languages(**{'label': "Tiếng Việt", 'iso': "vi", 'nllb': "vie_Latn"})
}

class LanguageUtils:
    @staticmethod
    def values():
        return list(LANGUAGE_MAP)

    @staticmethod
    def find_by_iso(iso: str) -> Languages | None:
        return next((lang for lang in LANGUAGE_MAP.values() if lang.iso == iso), None)

    @staticmethod
    def find_by_nllb(nllb: str) -> Languages | None:
        return next((lang for lang in LANGUAGE_MAP.values() if lang.nllb == nllb), None)