from rest_framework import serializers

from metadatax.common.serializers import InstitutionSerializer
from metadatax.equipment.models import Equipment
from .acoustic_detector_specification import AcousticDetectorSpecificationSerializer
from .hydrophone_specification import HydrophoneSpecificationSerializer
from .recorder_specification import RecorderSpecificationSerializer
from .storage_specification import StorageSpecificationSerializer


class EquipmentSerializer(serializers.ModelSerializer):
    owner = InstitutionSerializer()
    provider = InstitutionSerializer()

    storage_specification = StorageSpecificationSerializer()
    recorder_specification = RecorderSpecificationSerializer()
    hydrophone_specification = HydrophoneSpecificationSerializer()
    acoustic_detector_specification = AcousticDetectorSpecificationSerializer()

    class Meta:
        model = Equipment
        fields = "__all__"
