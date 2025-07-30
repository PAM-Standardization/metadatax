import graphene
from django_filters import FilterSet, NumberFilter
from graphene import ID, relay

from metadatax.ontology.models import Source
from metadatax.ontology.serializers import SourceSerializer
from metadatax.utils.schema import PostMutation, DeleteMutation, MxObjectType


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


class SourceNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = Source
        fields = "__all__"
        filterset_class = SourceFilter
        interfaces = (relay.Node,)


class PostSourceMutation(PostMutation):
    data = graphene.Field(SourceNode)

    class Meta:
        serializer_class = SourceSerializer
        model_class = Source
        model_operations = ["create", "update"]
        lookup_field = "id"


class DeleteSourceMutation(DeleteMutation):
    class Meta:
        model_class = Source
