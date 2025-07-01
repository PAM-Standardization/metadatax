from django_filters import FilterSet
from graphene import ID, relay
from graphene_django import DjangoObjectType

from metadatax.equipment.models import Maintenance


class MaintenanceFilter(FilterSet):
    class Meta:
        model = Maintenance
        fields = {
            "id": ["exact", "in"],
            "type_id": ["exact", "in"],
            "maintainer_id": ["exact", "in"],
            "platform_id": ["exact", "in"],
            "equipment_id": ["exact", "in"],
            "date": ["exact", "lt", "lte", "gt", "gte"],
        }


class MaintenanceNode(DjangoObjectType):
    id = ID(required=True)

    class Meta:
        model = Maintenance
        fields = "__all__"
        filterset_class = MaintenanceFilter
        interfaces = (relay.Node,)
