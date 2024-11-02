from abc import ABC, abstractmethod


class TokenFilter(ABC):

    @abstractmethod
    def filter(self, tokens: list[str]):
        ...