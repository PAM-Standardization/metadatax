from django_extended.schema.interfaces import ExtendedInterface
from django_extended.schema.types import ExtendedNode

from metadatax.equipment.models import PlatformType


class PlatformTypeNode(ExtendedNode):
    class Meta:
        model = PlatformType
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
            "is_mobile": ["exact"],
        }
        interfaces = (ExtendedInterface,)
