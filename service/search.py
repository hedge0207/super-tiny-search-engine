import json

from core.analyzer import Analyzer
from config.config import config


class Search:
    
    def search(self, query: str, analyzer: Analyzer):
        terms = analyzer.analyze(query)
        with open(config.segment_file_path, "r") as f:
            segment = json.load(f)
        
        hits = set()
        for token in terms:
            if segment.get(token):
                hits.update(set(segment[token]))
        
        with open(config.source_file_path, "r") as f:
            source = json.load(f)
        
        return [{"doc_id":doc_id, "text":source[doc_id]} for doc_id in hits]
