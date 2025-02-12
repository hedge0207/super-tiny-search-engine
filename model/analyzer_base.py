from pydantic import BaseModel
from model.common import TokenizerEnum, TokenFilterEnum


class _Analyzer(BaseModel):
    tokenizer: TokenizerEnum = TokenizerEnum.STANDARD
    token_filters: list[TokenFilterEnum] = []


class AnalyzerRequest(BaseModel):
    analyzer: _Analyzer = _Analyzer()
    