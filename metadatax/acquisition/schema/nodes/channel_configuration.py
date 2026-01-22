import graphene
from django_extension.schema.types import ExtendedNode

from metadatax.acquisition.models import ChannelConfiguration
from metadatax.equipment.schema import EquipmentNode
from .channel_configuration_specifications import ChannelConfigurationDetectorSpecificationNode, \
    ChannelConfigurationRecorderSpecificationNode


class ChannelConfigurationNode(ExtendedNode):
    storages = graphene.List(EquipmentNode)

    recorder_specification = ChannelConfigurationRecorderSpecificationNode()
    detector_specification = ChannelConfigurationDetectorSpecificationNode()

    class Meta:
        model = ChannelConfiguration
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "recorder_specification": ["isnull"],
            "detector_specification": ["isnull"],
            "continuous": ["exact"],
            "duty_cycle_on": ["exact", "lt", "lte", "gt", "gte"],
            "duty_cycle_off": ["exact", "lt", "lte", "gt", "gte"],
            "instrument_depth": ["exact", "lt", "lte", "gt", "gte"],
            "timezone": ["exact"],
            "harvest_starting_date": ["exact", "lt", "lte", "gt", "gte"],
            "harvest_ending_date": ["exact", "lt", "lte", "gt", "gte"],
        }
