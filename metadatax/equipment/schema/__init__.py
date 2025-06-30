from graphene import ObjectType, Field
from graphene_django.filter import DjangoFilterConnectionField

from metadatax.equipment.models import SDCardSpecification, RecorderSpecification, PlatformType, Platform, \
    MaintenanceType, Maintenance, HydrophoneSpecification, Equipment, AcousticDetectorSpecification
from .acoustic_detector_specification import AcousticDetectorSpecificationNode
from .equipment import EquipmentNode
from .hydrophone_specification import HydrophoneSpecificationNode
from .maintenance import MaintenanceNode
from .maintenance_type import MaintenanceTypeNode
from .platform import PlatformNode
from .platform_type import PlatformTypeNode
from .recorder_specification import RecorderSpecificationNode
from .sd_card_specification import SDCardSpecificationNode


class EquipmentQuery(ObjectType):
    all_acoustic_detector_specifications = DjangoFilterConnectionField(AcousticDetectorSpecificationNode)
    acoustic_detector_specification_by_id = Field(AcousticDetectorSpecificationNode)

    all_equipments = DjangoFilterConnectionField(EquipmentNode)
    equipment_by_id = Field(EquipmentNode)

    all_hydrophone_specifications = DjangoFilterConnectionField(HydrophoneSpecificationNode)
    hydrophone_specification_by_id = Field(HydrophoneSpecificationNode)

    all_maintenances = DjangoFilterConnectionField(MaintenanceNode)
    maintenance_by_id = Field(MaintenanceNode)

    all_maintenance_types = DjangoFilterConnectionField(MaintenanceTypeNode)
    maintenance_type_by_id = Field(MaintenanceTypeNode)

    all_platforms = DjangoFilterConnectionField(PlatformNode)
    platform_by_id = Field(PlatformNode)

    all_platform_types = DjangoFilterConnectionField(PlatformTypeNode)
    platform_type_by_id = Field(PlatformTypeNode)

    all_recorder_specifications = DjangoFilterConnectionField(RecorderSpecificationNode)
    recorder_specification_by_id = Field(RecorderSpecificationNode)

    all_sd_card_specifications = DjangoFilterConnectionField(SDCardSpecificationNode)
    sd_card_specification_by_id = Field(SDCardSpecificationNode)

    def resolve_acoustic_detector_specification_by_id(self, info, id: int):
        return AcousticDetectorSpecification.objects.get(pk=id)

    def resolve_equipment_by_id(self, info, id: int):
        return Equipment.objects.get(pk=id)

    def resolve_hydrophone_specification_by_id(self, info, id: int):
        return HydrophoneSpecification.objects.get(pk=id)

    def resolve_maintenance_by_id(self, info, id: int):
        return Maintenance.objects.get(pk=id)

    def resolve_maintenance_type_by_id(self, info, id: int):
        return MaintenanceType.objects.get(pk=id)

    def resolve_platform_by_id(self, info, id: int):
        return Platform.objects.get(pk=id)

    def resolve_platform_type_by_id(self, info, id: int):
        return PlatformType.objects.get(pk=id)

    def resolve_recorder_specification_by_id(self, info, id: int):
        return RecorderSpecification.objects.get(pk=id)

    def resolve_sd_card_specification_by_id(self, info, id: int):
        return SDCardSpecification.objects.get(pk=id)
