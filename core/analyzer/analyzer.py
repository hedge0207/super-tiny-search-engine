from abc import ABC, abstractmethod


class Analyzer(ABC):

    @abstractmethod
    def create_token_stream(self, text: str):
        ...
