"""Acquisition models for metadata app"""

import graphene
from django_extension.schema.types import ExtendedNode

from metadatax.acquisition.models.channel_configuration_specifications import ChannelConfigurationDetectorSpecification
from metadatax.data.schema import FileFormatNode
from metadatax.ontology.schema import LabelNode


class ChannelConfigurationDetectorSpecificationNode(ExtendedNode):
    output_formats = graphene.List(FileFormatNode)
    labels = graphene.List(LabelNode)

    class Meta:
        model = ChannelConfigurationDetectorSpecification
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "min_frequency": ["exact", "lt", "lte", "gt", "gte"],
            "max_frequency": ["exact", "lt", "lte", "gt", "gte"],
            "filter": ["exact", "icontains"],
            "configuration": ["exact", "icontains"],
        }
