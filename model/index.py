from pydantic import BaseModel
from model.analyzer_base import AnalyzerRequest


class Document(BaseModel):
    doc_id: str = None
    text: str


class IndexRequest(AnalyzerRequest):
    docs: list[Document]