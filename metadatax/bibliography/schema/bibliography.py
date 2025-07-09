from django_filters import FilterSet, CharFilter
from graphene import ID, relay, Scalar
from graphene_django import DjangoObjectType
from graphql.language import ast

from metadatax.bibliography.models import Bibliography


class StatusEnum(Scalar):
    @staticmethod
    def serialize(value):
        return Bibliography.Status(value).label

    @staticmethod
    def parse_literal(node, _variables=None):
        if isinstance(node, ast.StringValueNode):
            index = Bibliography.Status.labels.index(node.value)
            value = Bibliography.Status.values[index]
            return Bibliography.Status(value)

    @staticmethod
    def parse_value(value):
        index = Bibliography.Status.labels.index(value)
        value = Bibliography.Status.values[index]
        return Bibliography.Status(value)


class TypeEnum(Scalar):
    @staticmethod
    def serialize(value):
        return Bibliography.Type(value).label

    @staticmethod
    def parse_literal(node, _variables=None):
        if isinstance(node, ast.StringValueNode):
            index = Bibliography.Type.labels.index(node.value)
            value = Bibliography.Type.values[index]
            return Bibliography.Type(value)

    @staticmethod
    def parse_value(value):
        index = Bibliography.Type.labels.index(value)
        value = Bibliography.Type.values[index]
        return Bibliography.Type(value)


class BibliographyFilter(FilterSet):
    tags__name = CharFilter()

    class Meta:
        model = Bibliography
        fields = {
            "id": ["exact", "in"],
            "title": ["exact", "icontains"],
            "doi": ["exact"],
            "tags__name": ["exact", "in"],
            "status": ["exact"],
            "publication_date": ["exact", "lt", "lte", "gt", "gte"],
            "type": ["exact"],
        }


class BibliographyNode(DjangoObjectType):
    id = ID(required=True)
    type = TypeEnum(required=True)
    status = StatusEnum()

    class Meta:
        model = Bibliography
        fields = "__all__"
        filterset_class = BibliographyFilter
        interfaces = (relay.Node,)
