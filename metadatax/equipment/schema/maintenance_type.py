from django_filters import FilterSet, NumberFilter
from graphene import ID, relay

from metadatax.equipment.models import MaintenanceType
from metadatax.utils.schema import MxObjectType


class MaintenanceTypeFilter(FilterSet):
    maintenances__id = NumberFilter()

    class Meta:
        model = MaintenanceType
        fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
            "interval": ["exact", "lt", "lte", "gt", "gte"],
            "maintenances__id": ["exact", "in"],
        }


class MaintenanceTypeNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = MaintenanceType
        fields = "__all__"
        filterset_class = MaintenanceTypeFilter
        interfaces = (relay.Node,)
