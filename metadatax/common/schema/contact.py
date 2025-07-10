from django_filters import FilterSet, NumberFilter
from graphene import relay, ID
from graphene_django import DjangoObjectType

from metadatax.common.models import Contact


class ContactFilter(FilterSet):
    roles__id = NumberFilter()
    owned_equipments__id = NumberFilter()
    owned_platforms__id = NumberFilter()
    performed_maintenances__id = NumberFilter()
    provided_equipments__id = NumberFilter()
    provided_platforms__id = NumberFilter()

    class Model:
        model = Contact
        fields = {
            "id": ["exact", "in"],
            "roles__id": ["exact", "in"],
            "owned_equipments__id": ["exact", "in"],
            "owned_platforms__id": ["exact", "in"],
            "performed_maintenances__id": ["exact", "in"],
            "provided_equipments__id": ["exact", "in"],
            "provided_platforms__id": ["exact", "in"],
            "first_name": ["exact", "icontains"],
            "last_name": ["exact", "icontains"],
            "mail": ["exact", "icontains"],
            "website": ["exact", "icontains"],
        }


class ContactNode(DjangoObjectType):
    id = ID(required=True)

    class Meta:
        model = Contact
        fields = "__all__"
        filterset_class = ContactFilter
        interfaces = (relay.Node,)
