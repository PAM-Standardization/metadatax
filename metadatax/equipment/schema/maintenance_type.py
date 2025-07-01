from django_filters import FilterSet, NumberFilter
from graphene import ID, relay
from graphene_django import DjangoObjectType

from metadatax.equipment.models import MaintenanceType


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


class MaintenanceTypeNode(DjangoObjectType):
    id = ID(required=True)

    class Meta:
        model = MaintenanceType
        fields = "__all__"
        filterset_class = MaintenanceTypeFilter
        interfaces = (relay.Node,)
