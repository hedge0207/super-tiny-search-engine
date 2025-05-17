import re

from mecab import MeCab

from core.tokenizer.tokenizer import Tokenizer
from core.attribute import CharTermAttribute, CharTermAttributeImple


class KoreanTokenizer(Tokenizer):
    def __init__(self, text):
        super().__init__()
        self._text = text
        self._mecab = MeCab()
        self._term_attr: CharTermAttributeImple = self.add_attribute(CharTermAttribute)
    
    def _clean_text(self) -> str:
        return re.sub(r'[^a-zA-Zㄱ-ㅎ가-힣0-9 ]', '', self._text)
    
    def tokenize(self) -> list[str]:
        cleaned_text = self._clean_text()
        self._term_attr.terms = self._mecab.morphs(cleaned_text)