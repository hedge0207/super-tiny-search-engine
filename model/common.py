from enum import Enum

from core.tokenizer.standard import StandardTokenizer
from core.tokenizer.korean import KoreanTokenizer
from core.token_filter.lowercase import LowercaseFilter
from core.analyzer.standard import StandardAnalyzer
from core.analyzer.korean import KoreanAnalyzer


class TokenizerEnum(Enum):
    STANDARD = "standard"
    KOREAN = "korean"


class TokenFilterEnum(Enum):
    LOWERCASE = "lowercase"


class AnalyzerEnum(Enum):
    STANDARD = "standard"
    KOREAN = "korean"

ANALYZERS = {
    AnalyzerEnum.STANDARD: StandardAnalyzer,
    AnalyzerEnum.KOREAN: KoreanAnalyzer
}


TOKENIZERS = {
    "standard": StandardTokenizer,
    "korean": KoreanTokenizer
}


TOKEN_FILTER = {
    "lowercase": LowercaseFilter
}