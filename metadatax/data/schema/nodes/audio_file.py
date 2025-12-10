from django_extended.schema.interfaces import ExtendedInterface
from django_extended.schema.types import ExtendedNode
import graphene
import graphene_django_optimizer

from metadatax.common.schema import AccessibilityEnum
from metadatax.data.models import AudioFile


class AudioFileNode(ExtendedNode):
    accessibility = AccessibilityEnum()

    class Meta:
        model = AudioFile
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "filename": ["exact", "icontains"],
            "storage_location": ["exact", "icontains"],
            "file_size": ["exact", "lt", "lte", "gt", "gte"],
            "accessibility": ["exact"],
        }
        interfaces = (ExtendedInterface,)

    sampling_frequency = graphene.Int(required=True)

    @graphene_django_optimizer.resolver_hints()
    def resolve_sampling_frequency(self: AudioFile, info):
        return self.audio_properties.sampling_frequency

    initial_timestamp = graphene.Int(required=True)

    @graphene_django_optimizer.resolver_hints()
    def resolve_initial_timestamp(self: AudioFile, info):
        return self.audio_properties.initial_timestamp

    duration = graphene.Int(required=True)

    @graphene_django_optimizer.resolver_hints()
    def resolve_duration(self: AudioFile, info):
        return self.audio_properties.duration

    sample_depth = graphene.Int()

    @graphene_django_optimizer.resolver_hints()
    def resolve_sample_depth(self: AudioFile, info):
        return self.audio_properties.sample_depth
