from graphene import ObjectType
from graphene_django_pagination import DjangoPaginationConnectionField
from django_extension.schema.fields import ByIdField

from .nodes import *


class OntologyQuery(ObjectType):
    # Label
    all_labels = DjangoPaginationConnectionField(LabelNode)
    label_by_id = ByIdField(LabelNode)

    # Sound
    all_sounds = DjangoPaginationConnectionField(SoundNode)
    sound_by_id = ByIdField(SoundNode)
    # Source
    all_sources = DjangoPaginationConnectionField(SourceNode)
    source_by_id = ByIdField(SourceNode)

