from __future__ import annotations
from typing import Type, TypeVar


class Attribute:
    ...


class AttributeImpl(Attribute):
    ...

T = TypeVar("T", bound=Attribute)


class CharTermAttribute(Attribute):
    ...


class CharTermAttributeImple(AttributeImpl):
    def __init__(self):
        self._term_buffer = ['']*20
        self._length = 0
    
    @property
    def buffer(self):
        return self._term_buffer[:self._length]

    def add(self, offset: int, char: str):
        self._term_buffer[offset] = char
    
    def set_length(self, length: int):
        self._length = length


class AttributeSource:

    def __init__(self, input_source: AttributeSource=None):
        if input_source:
            self.attributes: dict[Type[Attribute], AttributeImpl] = input_source.attributes
        else:
            self.attributes: dict[Type[Attribute], AttributeImpl] = {}

    def add_attribute(self, att_class: Type[T]) -> T:
        att_impl = self.attributes.get(att_class)
        if att_impl is None:
            if att_class == CharTermAttribute:
                att_impl = CharTermAttributeImple()
            self.attributes[att_class] = att_impl
        return att_impl


class TokenStream(AttributeSource):
    def __init__(self, input: AttributeSource=None):
        super().__init__(input)


class TokenFilter(TokenStream):
    def __init__(self, input: TokenStream=None):
        super().__init__(input)


class LowercaseFilter(TokenFilter):
    def __init__(self, input: TokenStream=None):
        super().__init__(input)
        self._term_attr: CharTermAttributeImple = self.add_attribute(CharTermAttribute)
    
    @property
    def term_attr(self):
        return self._term_attr


class CustomTokenizer(TokenStream):
    def __init__(self):
        super().__init__()
        self._term_attr: CharTermAttributeImple = self.add_attribute(CharTermAttribute)
    
    @property
    def term_attr(self):
        return self._term_attr
    
    def print_token(self, string: str):
        offset = 0
        length = 0
        for char in string:
            if char == " ":
                self._term_attr.set_length(length)
                length = 0
                offset = 0
                print("".join(self._term_attr.buffer))
            else:
                self._term_attr.add(offset, char)
                offset += 1
                length += 1
        if length > 0:
            self._term_attr.set_length(length)
            print("".join(self._term_attr.buffer))


if __name__ == "__main__":
    stanadard_tokenizer = CustomTokenizer()
    lower_case_filter = LowercaseFilter(stanadard_tokenizer)
    stanadard_tokenizer.print_token("Hello World")
    assert stanadard_tokenizer.term_attr is lower_case_filter.term_attr