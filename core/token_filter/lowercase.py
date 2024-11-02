from core.token_filter.base import TokenFilter


class Lowercase(TokenFilter):

    def filter(self, tokens: list[str]):
        return [token.lower() for token in tokens]