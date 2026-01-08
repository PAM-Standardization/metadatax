from django_extended.schema.interfaces import ExtendedInterface
from django_extended.schema.types import ExtendedNode
import graphene

from metadatax.acquisition.models import ChannelConfiguration
from metadatax.equipment.schema import EquipmentNode


class ChannelConfigurationNode(ExtendedNode):
    storages = graphene.List(EquipmentNode)

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
        interfaces = (ExtendedInterface,)
