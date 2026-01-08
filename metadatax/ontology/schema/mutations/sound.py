from django_extended.schema.mutations import ModelPostMutation, ModelDeleteMutation
import graphene

from metadatax.ontology.models import Sound
from metadatax.ontology.serializers import SoundSerializer
from ..nodes import SoundNode


class PostSoundMutation(ModelPostMutation):
    data = graphene.Field(SoundNode)

    class Meta:
        serializer_class = SoundSerializer
        model_class = Sound
        model_operations = ["create", "update"]
        lookup_field = "id"


class DeleteSoundMutation(ModelDeleteMutation):
    class Meta:
        model_class = Sound
