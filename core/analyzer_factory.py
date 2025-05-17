from model.common import TOKENIZERS, TOKEN_FILTER, ANALYZERS
from core.analyzer.analyzer import Analyzer
from model.analyzer_base import AnalyzerRequest


def create_analyzer(request: AnalyzerRequest) -> Analyzer:
    return ANALYZERS[request.analyzer.analyzer]()