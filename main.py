from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, Depends
import uvicorn

from model.index import IndexRequest
from model.search import SearchRequest
from core.index import Index
from core.search import Search
from core.tokenizer.standard import StandardTokenizer
from utils import create_data_files


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_data_files()
    yield

app = FastAPI(lifespan=lifespan)

TOKENIZERS = {
    "standard": StandardTokenizer
}

@app.post("/index")
def index(request: IndexRequest, service: Annotated[Index, Depends(Index)]):
    service.index(request.docs, TOKENIZERS[request.tokenizer.value]())

@app.get("/search")
def search(request: SearchRequest, service: Annotated[Search, Depends(Search)]):
    return service.search(request.query, TOKENIZERS[request.tokenizer.value]())
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9090)