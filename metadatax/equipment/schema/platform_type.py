from django_filters import FilterSet, NumberFilter
from graphene import ID, relay

from metadatax.equipment.models import PlatformType
from metadatax.utils.schema import MxObjectType


class PlatformTypeFilter(FilterSet):
    platforms__id = NumberFilter()

    class Meta:
        model = PlatformType
        fields = {
            "id": ["exact", "in"],
            "platforms__id": ["exact", "in"],
            "name": ["exact", "icontains"],
            "is_mobile": ["exact"],
        }


class PlatformTypeNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = PlatformType
        fields = "__all__"
        filterset_class = PlatformTypeFilter
        interfaces = (relay.Node,)
