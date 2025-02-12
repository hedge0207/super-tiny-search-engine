import re

from mecab import MeCab

from core.tokenizer.base import Tokenizer


class KoreanTokenizer(Tokenizer):
    def __init__(self):
        self._mecab = MeCab()
    
    def tokenize(self, text: str) -> list[str]:
        text = re.sub(r'[^a-zA-Zㄱ-ㅎ가-힣0-9 ]', '', text)
        return self._mecab.morphs(text)