import re

from konlpy.tag import Kkma

from core.tokenizer.base import Tokenizer


class KoreanTokenizer(Tokenizer):
    def __init__(self):
        self._kkma = Kkma()
    
    def tokenize(self, text: str) -> list[str]:
        text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
        return self._kkma.morphs(text)