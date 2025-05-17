from abc import ABC, abstractmethod

from core.token_stream import TokenStream


class Analyzer(ABC):

    @abstractmethod
    def create_token_stream(self, text: str) -> TokenStream:
        ...
