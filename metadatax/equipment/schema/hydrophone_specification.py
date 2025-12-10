from django_filters import FilterSet
from graphene import ID, relay

from metadatax.equipment.models import HydrophoneSpecification
from metadatax.equipment.schema.hydrophone_directivity import HydrophoneDirectivityEnum
from metadatax.utils.schema import MxObjectType


class HydrophoneSpecificationFilter(FilterSet):

    class Meta:
        model = HydrophoneSpecification
        fields = {
            "id": ["exact", "in"],
            "directivity": ["exact"],
            "operating_min_temperature": ["exact", "lt", "lte", "gt", "gte"],
            "operating_max_temperature": ["exact", "lt", "lte", "gt", "gte"],
            "min_bandwidth": ["exact", "lt", "lte", "gt", "gte"],
            "max_bandwidth": ["exact", "lt", "lte", "gt", "gte"],
            "min_dynamic_range": ["exact", "lt", "lte", "gt", "gte"],
            "max_dynamic_range": ["exact", "lt", "lte", "gt", "gte"],
            "min_operating_depth": ["exact", "lt", "lte", "gt", "gte"],
            "max_operating_depth": ["exact", "lt", "lte", "gt", "gte"],
            "noise_floor": ["exact", "lt", "lte", "gt", "gte"],
        }


class HydrophoneSpecificationNode(MxObjectType):
    id = ID(required=True)
    directivity = HydrophoneDirectivityEnum()

    class Meta:
        model = HydrophoneSpecification
        fields = "__all__"
        filterset_class = HydrophoneSpecificationFilter
        interfaces = (relay.Node,)
