from django_filters import FilterSet, NumberFilter, CharFilter
from graphene import ID, relay, Scalar
from graphene_django import DjangoObjectType
from graphql.language import ast

from metadatax.common.models import ContactRole


class RoleEnum(Scalar):
    @staticmethod
    def serialize(value):
        return ContactRole.Type(value).label

    @staticmethod
    def parse_literal(node, _variables=None):
        if isinstance(node, ast.StringValueNode):
            index = ContactRole.Type.labels.index(node.value)
            value = ContactRole.Type.values[index]
            return ContactRole.Type(value)

    @staticmethod
    def parse_value(value):
        index = ContactRole.Type.labels.index(value)
        value = ContactRole.Type.values[index]
        return ContactRole.Type(value)


class ContactRoleFilter(FilterSet):
    contact__id = NumberFilter()
    contact__name = CharFilter()
    contact__mail = CharFilter()
    contact__website = CharFilter()
    deployments__id = NumberFilter()
    projects__id = NumberFilter()

    class Meta:
        model = ContactRole
        fields = {
            "id": ["exact", "in"],
            "role": ["exact"],
            "contact__id": ["exact", "in"],
            "contact__name": ["exact", "icontains"],
            "contact__mail": ["exact", "icontains"],
            "contact__website": ["exact", "icontains"],
            "deployments__id": ["exact", "in"],
            "projects__id": ["exact", "in"],
        }


class ContactRoleNode(DjangoObjectType):
    id = ID(required=True)
    role = RoleEnum()

    class Meta:
        model = ContactRole
        fields = "__all__"
        filterset_class = ContactRoleFilter
        interfaces = (relay.Node,)
