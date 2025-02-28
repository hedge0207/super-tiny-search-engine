from core.token_filter.token_filter import TokenFilter
from core.token_stream import TokenStream
from core.attribute import CharTermAttribute, CharTermAttributeImple


class LowercaseFilter(TokenFilter):
    def __init__(self, input: TokenStream=None):
        super().__init__(input)
        self._term_attr: CharTermAttributeImple = self.add_attribute(CharTermAttribute)
    
    def tokenize(self):
        self.token_stream.tokenize()
        self._term_attr.terms = [term.lower() for term in self._term_attr.terms]