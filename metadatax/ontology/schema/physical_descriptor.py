from django_filters import FilterSet, NumberFilter
from graphene import ID, relay, Scalar
from graphene_django import DjangoObjectType
from graphql.language import ast

from metadatax.ontology.models import PhysicalDescriptor, SignalShape, SignalPlurality


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


class PhysicalDescriptorFilter(FilterSet):
    label__id = NumberFilter()

    class Meta:
        model = PhysicalDescriptor
        fields = {
            "id": ["exact", "in"],
            "label__id": ["exact", "in"],
            "shape": [
                "exact",
            ],
            "plurality": [
                "exact",
            ],
            "min_frequency": ["exact", "lt", "lte", "gt", "gte"],
            "max_frequency": ["exact", "lt", "lte", "gt", "gte"],
            "mean_duration": ["exact", "lt", "lte", "gt", "gte"],
        }


class PhysicalDescriptorNode(DjangoObjectType):
    id = ID(required=True)
    shape = SignalShapeEnum()
    plurality = SignalShapeEnum()

    class Meta:
        model = PhysicalDescriptor
        fields = "__all__"
        filterset_class = PhysicalDescriptorFilter
        interfaces = (relay.Node,)
