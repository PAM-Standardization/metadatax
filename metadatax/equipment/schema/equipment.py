from django_filters import FilterSet, NumberFilter
from graphene import ID, relay

from metadatax.equipment.models import Equipment
from metadatax.utils.schema import MxObjectType


class EquipmentFilter(FilterSet):
    channel_configuration_detector_specifications__id = NumberFilter()
    channel_configuration_hydrophone_specifications__id = NumberFilter()
    channel_configuration_recorder_specifications__id = NumberFilter()
    channel_configurations__id = NumberFilter()
    maintenances__id = NumberFilter()

    class Meta:
        model = Equipment
        fields = {
            "id": ["exact", "in"],
            "model_id": ["exact", "in"],
            "serial_number": ["exact", "icontains"],
            "owner_id": ["exact", "in"],
            "purchase_date": ["exact", "lt", "lte", "gt", "gte"],
            "name": ["exact", "icontains"],
            "channel_configuration_detector_specifications__id": ["exact", "in"],
            "channel_configuration_hydrophone_specifications__id": ["exact", "in"],
            "channel_configuration_recorder_specifications__id": ["exact", "in"],
            "channel_configurations__id": ["exact", "in"],
            "maintenances__id": ["exact", "in"],
            "sensitivity": ["exact", "lt", "lte", "gt", "gte"],
        }


class EquipmentNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = Equipment
        fields = "__all__"
        filterset_class = EquipmentFilter
        interfaces = (relay.Node,)
