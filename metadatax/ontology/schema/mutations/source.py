from django_extended.schema.mutations import ModelDeleteMutation, ModelPostMutation
import graphene

from metadatax.ontology.models import Source
from metadatax.ontology.serializers import SourceSerializer
from ..nodes import SourceNode


class PostSourceMutation(ModelPostMutation):
    data = graphene.Field(SourceNode)

    class Meta:
        serializer_class = SourceSerializer
        model_class = Source
        model_operations = ["create", "update"]
        lookup_field = "id"


class DeleteSourceMutation(ModelDeleteMutation):
    class Meta:
        model_class = Source
