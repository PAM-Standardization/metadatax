import graphene
from django_extension.schema.types import ExtendedNode

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

    specifications = graphene.List(EquipmentSpecificationUnion)

    def resolve_specifications(self: EquipmentModel, info):
        return [
            s.specification
            for s in self.specification_relations.all()
        ]
