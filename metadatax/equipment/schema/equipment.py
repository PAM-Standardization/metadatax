from django_filters import FilterSet, NumberFilter
from graphene import ID, relay

from metadatax.equipment.models import Equipment
from metadatax.utils.schema import MxObjectType


class EquipmentFilter(FilterSet):
    maintenances__id = NumberFilter()

    class Meta:
        model = Equipment
        fields = {
            "id": ["exact", "in"],
            "model": ["exact", "in"],
            "serial_number": ["exact", "icontains"],
            "owner_id": ["exact", "in"],
            "purchase_date": ["exact", "lt", "lte", "gt", "gte"],
            "name": ["exact", "icontains"],
            "sensitivity": ["exact", "lt", "lte", "gt", "gte", "isnull"],
        }


class EquipmentNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = Equipment
        fields = "__all__"
        filterset_class = EquipmentFilter
        interfaces = (relay.Node,)
