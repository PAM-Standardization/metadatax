from graphene import ObjectType

from .platform_type import PlatformTypeMutation
from .platform import PlatformMutation
from .equipment import EquipmentMutation as _EquipmentMutation
from .equipment_model import CreateEquipmentModel


class EquipmentMutation(ObjectType):
    platform_type = PlatformTypeMutation.Field()
    platform = PlatformMutation.Field()

    equipment = _EquipmentMutation.Field()
    create_equipment_model = CreateEquipmentModel.Field()
