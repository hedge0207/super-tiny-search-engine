from pydantic import BaseModel
from model.common import Tokenizer


class SearchRequest(BaseModel):
    query: str
    tokenizer: Tokenizer