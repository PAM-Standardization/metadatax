from graphene import relay
import graphene.types

from metadatax.equipment.models import AcousticDetectorSpecification, HydrophoneSpecification, StorageSpecification, \
    RecorderSpecification
from .acoustic_detector_specification import AcousticDetectorSpecificationNode
from .hydrophone_specification import HydrophoneSpecificationNode
from .storage_specification import StorageSpecificationNode
from .recorder_specification import RecorderSpecificationNode


class EquipmentSpecificationUnion(graphene.types.Union):
    class Meta:
        types = [
            AcousticDetectorSpecificationNode,
            HydrophoneSpecificationNode,
            StorageSpecificationNode,
            RecorderSpecificationNode,
        ]

    @classmethod
    def resolve_type(cls, instance: any, info):
        if isinstance(instance, AcousticDetectorSpecification):
            return AcousticDetectorSpecificationNode
        if isinstance(instance, HydrophoneSpecification):
            return HydrophoneSpecificationNode
        if isinstance(instance, StorageSpecification):
            return StorageSpecificationNode
        if isinstance(instance, RecorderSpecification):
            return RecorderSpecificationNode
        return super().resolve_type(instance, info)


class EquipmentSpecificationUnionConnection(relay.Connection):
    class Meta:
        node = EquipmentSpecificationUnion
