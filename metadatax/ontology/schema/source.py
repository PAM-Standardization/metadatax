from django_filters import FilterSet, NumberFilter
from graphene import ID, relay
from graphene_django import DjangoObjectType

from metadatax.ontology.models import Source


class SourceFilter(FilterSet):
    labels__id = NumberFilter()
    children__id = NumberFilter()

    class Meta:
        model = Source
        fields = {
            "id": ["exact", "in"],
            "parent_id": ["exact", "in"],
            "children__id": ["exact", "in"],
            "labels__id": ["exact", "in"],
            "english_name": ["exact", "icontains"],
            "latin_name": ["exact", "icontains"],
            "french_name": ["exact", "icontains"],
            "code_name": ["exact", "icontains"],
            "taxon": ["exact", "icontains"],
        }


class SourceNode(DjangoObjectType):
    id = ID(required=True)

    class Meta:
        model = Source
        fields = "__all__"
        filterset_class = SourceFilter
        interfaces = (relay.Node,)
