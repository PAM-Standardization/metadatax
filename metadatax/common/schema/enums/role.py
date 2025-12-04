from graphene import Scalar
from graphql.language import ast

from metadatax.common.models.enums import Role


class RoleEnum(Scalar):
    @staticmethod
    def serialize(value):
        return Role(value).label

    @staticmethod
    def parse_literal(node, _variables=None):
        if isinstance(node, ast.StringValueNode):
            index = Role.labels.index(node.value)
            value = Role.values[index]
            return Role(value)

    @staticmethod
    def parse_value(value):
        index = Role.labels.index(value)
        value = Role.values[index]
        return Role(value)
