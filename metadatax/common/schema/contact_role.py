from django_filters import FilterSet, NumberFilter, CharFilter
from graphene import ID, relay, Scalar
from graphql.language import ast

from metadatax.common.models import ContactRole
from metadatax.utils.schema import MxObjectType


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
    contact__first_name = CharFilter()
    contact__last_name = CharFilter()
    contact__mail = CharFilter()
    contact__website = CharFilter()
    institution__id = NumberFilter()
    institution__name = CharFilter()
    institution__mail = CharFilter()
    institution__website = CharFilter()
    deployments__id = NumberFilter()
    projects__id = NumberFilter()

    class Meta:
        model = ContactRole
        fields = {
            "id": ["exact", "in"],
            "role": ["exact"],
            "contact__id": ["exact", "in"],
            "contact__first_name": ["exact", "icontains"],
            "contact__last_name": ["exact", "icontains"],
            "contact__mail": ["exact", "icontains"],
            "contact__website": ["exact", "icontains"],
            "institution__id": ["exact", "in"],
            "institution__name": ["exact", "icontains"],
            "institution__mail": ["exact", "icontains"],
            "institution__website": ["exact", "icontains"],
            "deployments__id": ["exact", "in"],
            "projects__id": ["exact", "in"],
        }


class ContactRoleNode(MxObjectType):
    id = ID(required=True)
    role = RoleEnum()

    class Meta:
        model = ContactRole
        fields = "__all__"
        filterset_class = ContactRoleFilter
        interfaces = (relay.Node,)
