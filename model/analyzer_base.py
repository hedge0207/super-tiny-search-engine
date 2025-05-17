from pydantic import BaseModel
from model.common import AnalyzerEnum, TokenizerEnum, TokenFilterEnum


class _Analyzer(BaseModel):
    analyzer : AnalyzerEnum = AnalyzerEnum.STANDARD
    tokenizer: TokenizerEnum = None
    token_filters: list[TokenFilterEnum] = []


class AnalyzerRequest(BaseModel):
    analyzer: _Analyzer = _Analyzer()
    