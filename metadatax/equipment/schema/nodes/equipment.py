from django_extended.schema.interfaces import ExtendedInterface
from django_extended.schema.types import ExtendedNode

from metadatax.common.schema.unions import ContactUnion
from metadatax.equipment.models import Equipment
from .equipment_model import EquipmentModelNode


class EquipmentNode(ExtendedNode):
    model = EquipmentModelNode()

    class Meta:
        model = Equipment
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "serial_number": ["exact", "icontains"],
            "purchase_date": ["exact", "lt", "lte", "gt", "gte"],
            "name": ["exact", "icontains"],
            "sensitivity": ["exact", "lt", "lte", "gt", "gte", "isnull"],
        }
        interfaces = (ExtendedInterface,)

    owner = ContactUnion()

    def resolve_owner(self: Equipment, info):
        return self.owner
