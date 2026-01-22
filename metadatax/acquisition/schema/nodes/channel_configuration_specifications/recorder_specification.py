"""Acquisition models for metadata app"""

import graphene
from django_extension.schema.types import ExtendedNode

from metadatax.acquisition.models.channel_configuration_specifications import ChannelConfigurationRecorderSpecification
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
