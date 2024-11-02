from model.common import TOKENIZERS, TOKEN_FILTER
from core.tokenizer.base import Tokenizer
from core.token_filter.base import TokenFilter
from model.analyzer_base import AnalyzerRequest


class Analyzer:

    def __init__(self, tokenizer: Tokenizer, token_filters: list[TokenFilter]):
        self._tokenizer = tokenizer
        self._token_filters = token_filters

    def analyze(self, text):
        tokens = self._tokenizer.tokenize(text)

        for token_filter in self._token_filters:
            tokens = token_filter.filter(tokens)

        return tokens


def analyzer_factory(request: AnalyzerRequest) -> Analyzer:
    return Analyzer(
        TOKENIZERS[request.analyzer.tokenizer.value](), 
        [TOKEN_FILTER[token_filter.value]() for token_filter in request.analyzer.token_filters]
    )