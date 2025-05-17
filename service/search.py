import json

from core.attribute import CharTermAttribute
from core.analyzer.analyzer import Analyzer
from config.config import config


class Search:
    
    def search(self, query: str, analyzer: Analyzer):
        token_stream = analyzer.create_token_stream(query)
        token_stream.tokenize()
        terms = token_stream.get_attribute(CharTermAttribute).terms
        with open(config.segment_file_path, "r") as f:
            segment = json.load(f)
        
        hits = set()
        for token in terms:
            if segment.get(token):
                hits.update(set(segment[token]))
        
        with open(config.source_file_path, "r") as f:
            source = json.load(f)
        
        return [{"doc_id":doc_id, "text":source[doc_id]} for doc_id in hits]
