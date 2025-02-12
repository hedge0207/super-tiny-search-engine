from enum import Enum

from core.tokenizer.standard import StandardTokenizer
from core.tokenizer.korean import KoreanTokenizer
from core.token_filter.lowercase import Lowercase


class TokenizerEnum(Enum):
    STANDARD = "standard"
    KOREAN = "korean"


class TokenFilterEnum(Enum):
    LOWERCASE = "lowercase"


TOKENIZERS = {
    "standard": StandardTokenizer,
    "korean":KoreanTokenizer
}


TOKEN_FILTER = {
    "lowercase": Lowercase
}