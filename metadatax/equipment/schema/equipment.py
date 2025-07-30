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
            "model": ["exact", "icontains"],
            "serial_number": ["exact", "icontains"],
            "owner_id": ["exact", "in"],
            "provider_id": ["exact", "in"],
            "storage_specification": ["isnull"],
            "recorder_specification": ["isnull"],
            "hydrophone_specification": ["isnull"],
            "acoustic_detector_specification": ["isnull"],
            "purchase_date": ["exact", "lt", "lte", "gt", "gte"],
            "name": ["exact", "icontains"],
            "battery_slots_count": ["exact", "lt", "lte", "gt", "gte"],
            "battery_type": ["exact", "icontains"],
            "cables": ["exact", "icontains"],
            "channel_configuration_detector_specifications__id": ["exact", "in"],
            "channel_configuration_hydrophone_specifications__id": ["exact", "in"],
            "channel_configuration_recorder_specifications__id": ["exact", "in"],
            "channel_configurations__id": ["exact", "in"],
            "maintenances__id": ["exact", "in"],
        }


class EquipmentNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = Equipment
        fields = "__all__"
        filterset_class = EquipmentFilter
        interfaces = (relay.Node,)
