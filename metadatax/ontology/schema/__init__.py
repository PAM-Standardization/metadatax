import graphene
from graphene import ObjectType, Field
from graphene_django_pagination import DjangoPaginationConnectionField

from metadatax.ontology.models import Label, Sound, Source
from .label import LabelNode
from .sound import SoundNode, PostSoundMutation, DeleteSoundMutation
from .source import SourceNode, PostSourceMutation, DeleteSourceMutation


class OntologyQuery(ObjectType):

    all_labels = DjangoPaginationConnectionField(LabelNode)
    label_by_id = Field(LabelNode, id=graphene.ID(required=True))

    all_sounds = DjangoPaginationConnectionField(SoundNode)
    sound_by_id = Field(SoundNode, id=graphene.ID(required=True))

    all_sources = DjangoPaginationConnectionField(SourceNode)
    source_by_id = Field(SourceNode, id=graphene.ID(required=True))

    def resolve_label_by_id(self, info, id):
        return Label.objects.get(pk=id)

    def resolve_sound_by_id(self, info, id):
        return Sound.objects.get(pk=id)

    def resolve_source_by_id(self, info, id):
        return Source.objects.get(pk=id)


class OntologyMutation(ObjectType):
    post_source = PostSourceMutation.Field()
    delete_source = DeleteSourceMutation.Field()

    post_sound = PostSoundMutation.Field()
    delete_sound = DeleteSoundMutation.Field()
