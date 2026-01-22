from django_extension.schema.fields import ByIdField
from graphene import ObjectType
from graphene_django_pagination import DjangoPaginationConnectionField

from .nodes import *


class EquipmentQuery(ObjectType):
    # Maintenance
    all_maintenances = DjangoPaginationConnectionField(MaintenanceNode)
    maintenance_by_id = ByIdField(MaintenanceNode)
    all_maintenance_types = DjangoPaginationConnectionField(MaintenanceTypeNode)

    # Platform
    all_platforms = DjangoPaginationConnectionField(PlatformNode)
    platform_by_id = ByIdField(PlatformNode)
    all_platform_types = DjangoPaginationConnectionField(PlatformTypeNode)

    # Equipment
    all_equipments = DjangoPaginationConnectionField(EquipmentNode)
    equipment_by_id = ByIdField(EquipmentNode)
    all_equipment_models = DjangoPaginationConnectionField(EquipmentModelNode)
