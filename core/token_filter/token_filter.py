from core.token_stream import TokenStream


class TokenFilter(TokenStream):
    def __init__(self, input: TokenStream=None):
        super().__init__(input)
        self.token_stream = input