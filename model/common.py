from enum import Enum

from core.tokenizer.standard import StandardTokenizer
from core.token_filter.lowercase import Lowercase


class TokenizerEnum(Enum):
    STANDARD = "standard"


class TokenFilterEnum(Enum):
    LOWERCASE = "lowercase"


TOKENIZERS = {
    "standard": StandardTokenizer
}


TOKEN_FILTER = {
    "lowercase": Lowercase
}