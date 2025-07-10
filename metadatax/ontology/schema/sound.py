import graphene
from django_filters import FilterSet, NumberFilter
from graphene import ID, relay
from graphene_django import DjangoObjectType

from metadatax.ontology.models import Sound
from metadatax.ontology.serializers import SoundSerializer
from metadatax.utils.schema import DeleteMutation, PostMutation


class SoundFilter(FilterSet):
    labels__id = NumberFilter()
    children__id = NumberFilter()
    associated_names__id = NumberFilter()

    class Meta:
        model = Sound
        fields = {
            "id": ["exact", "in"],
            "parent_id": ["exact", "in"],
            "children__id": ["exact", "in"],
            "labels__id": ["exact", "in"],
            "associated_names__id": ["exact", "in"],
            "english_name": ["exact", "icontains"],
            "french_name": ["exact", "icontains"],
            "code_name": ["exact", "icontains"],
            "taxon": ["exact", "icontains"],
        }


class SoundNode(DjangoObjectType):
    id = ID(required=True)

    class Meta:
        model = Sound
        fields = "__all__"
        filterset_class = SoundFilter
        interfaces = (relay.Node,)


class PostSoundMutation(PostMutation):
    data = graphene.Field(SoundNode)

    class Meta:
        serializer_class = SoundSerializer
        model_class = Sound
        model_operations = ["create", "update"]
        lookup_field = "id"


class DeleteSoundMutation(DeleteMutation):
    class Meta:
        model_class = Sound
