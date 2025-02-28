from __future__ import annotations
from typing import Type, TypeVar


class Attribute:
    ...


T = TypeVar("T", bound=Attribute)


class AttributeImpl(Attribute):
    ...


class CharTermAttribute(Attribute):
    ...


class CharTermAttributeImple(AttributeImpl):
    def __init__(self):
        self._terms = []

    @property
    def terms(self):
        return self._terms
    
    @terms.setter
    def terms(self, terms: list[str]):
        self._terms = terms
    
    


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