from django_extended.schema.interfaces import ExtendedInterface
from django_extended.schema.types import ExtendedNode

from metadatax.equipment.models import RecorderSpecification


class RecorderSpecificationNode(ExtendedNode):
    class Meta:
        model = RecorderSpecification
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "channels_count": ["exact", "lt", "lte", "gt", "gte"],
            "storage_slots_count": ["exact", "lt", "lte", "gt", "gte"],
            # "storage_maximum_capacity": ["exact", "lt", "lte", "gt", "gte"], # TODO
            "storage_type": ["exact", "icontains"],
        }
        interfaces = [ExtendedInterface]
