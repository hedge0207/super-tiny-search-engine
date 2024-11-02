import re

from core.tokenizer.base import Tokenizer


class StandardTokenizer(Tokenizer):
    
    def tokenize(self, text: str) -> list[str]:
        text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
        return text.split()