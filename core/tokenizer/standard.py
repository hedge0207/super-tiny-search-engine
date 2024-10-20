from core.tokenizer.base import Tokenizer


class StandardTokenizer(Tokenizer):
    
    def tokenize(self, text: str) -> list[str]:
        return text.split()