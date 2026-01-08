from django_extended.schema.interfaces import ExtendedInterface
from django_extended.schema.types import ExtendedNode

from metadatax.equipment.models import HydrophoneSpecification
from ...enums import HydrophoneDirectivityEnum


class HydrophoneSpecificationNode(ExtendedNode):
    directivity = HydrophoneDirectivityEnum()

    class Meta:
        model = HydrophoneSpecification
        fields = "__all__"
        filter_fields = {
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
        interfaces = (ExtendedInterface,)
