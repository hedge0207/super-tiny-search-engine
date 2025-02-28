import re

from core.tokenizer.tokenizer import Tokenizer
from core.attribute import CharTermAttribute, CharTermAttributeImple


class StandardTokenizer(Tokenizer):
    def __init__(self, text):
        super().__init__()
        self._text = text
        self._term_attr: CharTermAttributeImple = self.add_attribute(CharTermAttribute)
    
    def tokenize(self):
        text = re.sub(r'[^a-zA-Zㄱ-ㅎ가-힣0-9 ]', '', self._text)
        self._term_attr.terms = text.split()