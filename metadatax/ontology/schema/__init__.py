from graphene import ObjectType, Field
from graphene_django.filter import DjangoFilterConnectionField

from metadatax.ontology.models import Label, PhysicalDescriptor, Sound, Source
from .label import LabelNode
from .physical_descriptor import PhysicalDescriptorNode
from .sound import SoundNode
from .source import SourceNode


class OntologyQuery(ObjectType):

    all_labels = DjangoFilterConnectionField(LabelNode)
    label_by_id = Field(LabelNode)

    all_physical_descriptors = DjangoFilterConnectionField(PhysicalDescriptorNode)
    physical_descriptor_by_id = Field(PhysicalDescriptorNode)

    all_sounds = DjangoFilterConnectionField(SoundNode)
    sound_by_id = Field(SoundNode)

    all_sources = DjangoFilterConnectionField(SourceNode)
    source_by_id = Field(SourceNode)

    def resolve_label_by_id(self, info, id):
        return Label.objects.get(pk=id)

    def resolve_physical_descriptor_by_id(self, info, id):
        return PhysicalDescriptor.objects.get(pk=id)

    def resolve_sound_by_id(self, info, id):
        return Sound.objects.get(pk=id)

    def resolve_source_by_id(self, info, id):
        return Source.objects.get(pk=id)
