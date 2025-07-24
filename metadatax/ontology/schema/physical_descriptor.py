from graphene import Scalar
from graphql.language import ast

from metadatax.ontology.models import SignalShape, SignalPlurality


class SignalShapeEnum(Scalar):
    @staticmethod
    def serialize(value):
        return SignalShape(value).label

    @staticmethod
    def parse_literal(node, _variables=None):
        if isinstance(node, ast.StringValueNode):
            index = SignalShape.labels.index(node.value)
            value = SignalShape.values[index]
            return SignalShape(value)

    @staticmethod
    def parse_value(value):
        index = SignalShape.labels.index(value)
        value = SignalShape.values[index]
        return SignalShape(value)


class SignalPluralityEnum(Scalar):
    @staticmethod
    def serialize(value):
        return SignalPlurality(value).label

    @staticmethod
    def parse_literal(node, _variables=None):
        if isinstance(node, ast.StringValueNode):
            index = SignalPlurality.labels.index(node.value)
            value = SignalPlurality.values[index]
            return SignalPlurality(value)

    @staticmethod
    def parse_value(value):
        index = SignalPlurality.labels.index(value)
        value = SignalPlurality.values[index]
        return SignalPlurality(value)
