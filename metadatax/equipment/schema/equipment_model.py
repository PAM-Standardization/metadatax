from graphene import ID, relay

from metadatax.common.schema import InstitutionNode
from metadatax.equipment.models import EquipmentModel
from metadatax.utils.schema import MxObjectType


class EquipmentModelNode(MxObjectType):
    id = ID(required=True)
    provider = InstitutionNode()

    class Meta:
        model = EquipmentModel
        fields = "__all__"
        filter_fields = {}
        interfaces = (relay.Node,)
