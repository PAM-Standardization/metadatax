from graphene import Scalar
from graphql.language import ast

from metadatax.equipment.models import HydrophoneDirectivity


class HydrophoneDirectivityEnum(Scalar):
    @staticmethod
    def serialize(value):
        return HydrophoneDirectivity(value).label

    @staticmethod
    def parse_literal(node, _variables=None):
        if isinstance(node, ast.StringValueNode):
            index = HydrophoneDirectivity.labels.index(node.value)
            value = HydrophoneDirectivity.values[index]
            return HydrophoneDirectivity(value)

    @staticmethod
    def parse_value(value):
        index = HydrophoneDirectivity.labels.index(value)
        value = HydrophoneDirectivity.values[index]
        return HydrophoneDirectivity(value)
