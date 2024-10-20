from pydantic import BaseModel
from model.common import Tokenizer


class Document(BaseModel):
    doc_id: str = None
    text: str


class IndexRequest(BaseModel):
    docs: list[Document]
    tokenizer: Tokenizer