"""Acquisition models for metadata app"""

from django_extended.schema.interfaces import ExtendedInterface
from django_extended.schema.types import ExtendedNode
import graphene

from metadatax.acquisition.models import ChannelConfigurationRecorderSpecification
from metadatax.data.schema import FileFormatNode


class ChannelConfigurationRecorderSpecificationNode(ExtendedNode):
    recording_formats = graphene.List(FileFormatNode)

    class Meta:
        model = ChannelConfigurationRecorderSpecification
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "sampling_frequency": ["exact", "lt", "lte", "gt", "gte"],
            "sample_depth": ["exact", "lt", "lte", "gt", "gte"],
            "gain": ["exact", "lt", "lte", "gt", "gte"],
            "channel_name": ["exact", "icontains"],
        }
        interfaces = (ExtendedInterface,)
