from graphene import Scalar
from graphql.language import ast

from metadatax.common.models.enums import Accessibility


class AccessibilityEnum(Scalar):
    @staticmethod
    def serialize(value):
        return Accessibility(value).label

    @staticmethod
    def parse_literal(node, _variables=None):
        if isinstance(node, ast.StringValueNode):
            index = Accessibility.labels.index(node.value)
            value = Accessibility.values[index]
            return Accessibility(value)

    @staticmethod
    def parse_value(value):
        index = Accessibility.labels.index(value)
        value = Accessibility.values[index]
        return Accessibility(value)
