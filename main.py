from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, Depends
import uvicorn

from model.index import IndexRequest
from model.search import SearchRequest
from model.analyze import AnalyzeRequest
from service.index import Index
from service.search import Search
from core.analyzer.analyzer import Analyzer
from core.analyzer_factory import create_analyzer
from core.attribute import CharTermAttribute
from utils import create_data_files


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_data_files()
    yield


app = FastAPI(lifespan=lifespan)

AnalyzerDep = Annotated[Analyzer, Depends(create_analyzer)]

@app.post("/index")
def index(request: IndexRequest, analyzer: AnalyzerDep, service: Annotated[Index, Depends(Index)]):
    service.index(request.docs, analyzer)

@app.get("/search")
def search(request: SearchRequest,  analyzer: AnalyzerDep, service: Annotated[Search, Depends(Search)]):
    return service.search(request.query, analyzer)

@app.get("/analyze")
def analyze(request: AnalyzeRequest, analyzer: AnalyzerDep):
    token_stream = analyzer.create_token_stream(request.text)
    token_stream.tokenize()
    return token_stream.get_attribute(CharTermAttribute)
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9090)