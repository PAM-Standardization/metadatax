"""Acquisition models for metadata app"""

from django_extended.schema.interfaces import ExtendedInterface
from django_extended.schema.types import ExtendedNode
import graphene

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
        interfaces = (ExtendedInterface,)
