from django_filters import FilterSet
from graphene import ID, relay

from metadatax.equipment.models import Maintenance
from metadatax.utils.schema import MxObjectType


class MaintenanceFilter(FilterSet):
    class Meta:
        model = Maintenance
        fields = {
            "id": ["exact", "in"],
            "type_id": ["exact", "in"],
            "maintainer_id": ["exact", "in"],
            "maintainer_institution_id": ["exact", "in"],
            "platform_id": ["exact", "in"],
            "equipment_id": ["exact", "in"],
            "date": ["exact", "lt", "lte", "gt", "gte"],
        }


class MaintenanceNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = Maintenance
        fields = "__all__"
        filterset_class = MaintenanceFilter
        interfaces = (relay.Node,)
