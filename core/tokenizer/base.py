from abc import ABCMeta, abstractmethod


class Tokenizer(metaclass=ABCMeta):

    @abstractmethod
    def tokenize(self, text: str) -> list[str]:
        pass