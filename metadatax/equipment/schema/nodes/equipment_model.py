from django_extended.schema.interfaces import ExtendedInterface
from django_extended.schema.types import ExtendedNode
import graphene

from metadatax.equipment.models import EquipmentModel
from metadatax.equipment.schema.nodes import EquipmentSpecificationUnion


class EquipmentModelNode(ExtendedNode):
    class Meta:
        model = EquipmentModel
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "name": ["exact", "in"],
            "battery_slots_count": ["exact", "lt", "lte", "gt", "gte", "isnull"],
            "battery_type": ["exact", "in"],
            "cables": ["exact", "in"],
        }
        interfaces = (ExtendedInterface,)

    specifications = graphene.List(EquipmentSpecificationUnion)

    def resolve_specifications(self: EquipmentModel, info):
        return [
            s.specification
            for s in self.specification_relations.all()
        ]
