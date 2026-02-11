from django_extension.schema.types import ExtendedNode

from metadatax.equipment.models import MaintenanceType


class MaintenanceTypeNode(ExtendedNode):
    class Meta:
        model = MaintenanceType
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
            "interval": ["exact", "lt", "lte", "gt", "gte"],
        }
