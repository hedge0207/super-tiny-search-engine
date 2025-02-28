from abc import abstractmethod, ABC

from core.attribute import AttributeSource


class TokenStream(AttributeSource, ABC):
    def __init__(self, input: AttributeSource=None):
        super().__init__(input)
    
    @abstractmethod
    def tokenize(self):
        ...
    