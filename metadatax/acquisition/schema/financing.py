from graphene import Scalar
from graphql.language import ast

from metadatax.acquisition.models import Financing


class FinancingEnum(Scalar):
    @staticmethod
    def serialize(value):
        return Financing(value).label

    @staticmethod
    def parse_literal(node, _variables=None):
        if isinstance(node, ast.StringValueNode):
            index = Financing.labels.index(node.value)
            value = Financing.values[index]
            return Financing(value)

    @staticmethod
    def parse_value(value):
        index = Financing.labels.index(value)
        value = Financing.values[index]
        return Financing(value)
