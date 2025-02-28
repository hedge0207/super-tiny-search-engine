from core.analyzer.analyzer import Analyzer
from core.tokenizer.standard import StandardTokenizer
from core.token_filter.lowercase import LowercaseFilter
from core.token_stream import TokenStream

class StandardAnalyzer(Analyzer):
    def create_token_stream(self, text) -> TokenStream:
        token_stream = StandardTokenizer(text)
        token_stream = LowercaseFilter(token_stream)
        return token_stream