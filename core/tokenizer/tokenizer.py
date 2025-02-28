from core.token_stream import TokenStream


class Tokenizer(TokenStream):
    def __init__(self, input: TokenStream=None):
        super().__init__(input)