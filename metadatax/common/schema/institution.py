from django_filters import FilterSet, NumberFilter
from graphene import relay, ID

from metadatax.common.models import Contact, Institution
from metadatax.utils.schema import MxObjectType


class InstitutionFilter(FilterSet):
    bibliography_authors__id = NumberFilter()
    contacts__id = NumberFilter()
    provided_equipments__id = NumberFilter()
    owned_equipments__id = NumberFilter()
    provided_platforms__id = NumberFilter()
    owned_platforms__id = NumberFilter()
    roles__id = NumberFilter()
    performed_maintenances__id = NumberFilter()

    class Model:
        model = Contact
        fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
            "city": ["exact", "icontains"],
            "country": ["exact", "icontains"],
            "mail": ["exact", "icontains"],
            "website": ["exact", "icontains"],
            "bibliography_authors__id": ["exact", "in"],
            "contacts__id": ["exact", "in"],
            "provided_equipments__id": ["exact", "in"],
            "owned_equipments__id": ["exact", "in"],
            "provided_platforms__id": ["exact", "in"],
            "owned_platforms__id": ["exact", "in"],
            "roles__id": ["exact", "in"],
            "performed_maintenances__id": ["exact", "in"],
        }


class InstitutionNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = Institution
        fields = "__all__"
        filterset_class = InstitutionFilter
        interfaces = (relay.Node,)
