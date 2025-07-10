from django_filters import FilterSet, NumberFilter
from graphene import relay, ID
from graphene_django import DjangoObjectType

from metadatax.common.models import Contact, Institution


class InstitutionFilter(FilterSet):
    bibliography_authors__id = NumberFilter()
    contacts__id = NumberFilter()

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
        }


class InstitutionNode(DjangoObjectType):
    id = ID(required=True)

    class Meta:
        model = Institution
        fields = "__all__"
        filterset_class = InstitutionFilter
        interfaces = (relay.Node,)
