import uuid
import json

from core.analyzer.analyzer import Analyzer
from core.attribute import CharTermAttribute
from model.index import Document
from config.config import config


class Index:

    def _create_uuid(self):
        # elasticsearch/server/src/main/java/org/elasticsearch/common/TimeBasedUUIDGenerator
        return uuid.uuid1().hex


    def index(self, docs: list[Document], analyzer: Analyzer):
        with open(config.segment_file_path, "r") as f:
            segment = json.load(f)

        with open(config.source_file_path, "r") as f:
            source = json.load(f)
        
        for doc in docs:
            token_stream = analyzer.create_token_stream(doc.text)
            doc_id = doc.doc_id or self._create_uuid()
            source[doc_id] = doc.text
            token_stream.tokenize()
            tokens = token_stream.get_attribute(CharTermAttribute).terms
            for token in tokens:
                if token in segment:
                    if doc_id not in segment[token]:
                        segment[token].append(doc_id)
                else:
                    segment[token] = [doc_id]
        
        with open(config.segment_file_path, "w") as f:
            json.dump(segment, f, ensure_ascii=False, indent="\t")
        
        with open(config.source_file_path, "w") as f:
            json.dump(source, f, ensure_ascii=False, indent="\t")