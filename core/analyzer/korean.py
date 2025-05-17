from core.analyzer.analyzer import Analyzer
from core.tokenizer.korean import KoreanTokenizer
from core.token_stream import TokenStream


class KoreanAnalyzer(Analyzer):
    def create_token_stream(self, text) -> TokenStream:
        token_stream = KoreanTokenizer(text)
        return token_stream