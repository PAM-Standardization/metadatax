from rest_framework import serializers

from metadatax_common.serializers import ContactSerializer
from metadatax_equipment.models import Equipment
from .acoustic_detector_specification import AcousticDetectorSpecificationSerializer
from .hydrophone_specification import HydrophoneSpecificationSerializer
from .recorder_specification import RecorderSpecificationSerializer
from .sd_card_specification import SDCardSpecificationSerializer


class EquipmentSerializer(serializers.ModelSerializer):
    owner = ContactSerializer()
    provider = ContactSerializer()

    sd_card_specification = SDCardSpecificationSerializer()
    recorder_specification = RecorderSpecificationSerializer()
    hydrophone_specification = HydrophoneSpecificationSerializer()
    acoustic_detector_specification = AcousticDetectorSpecificationSerializer()

    class Meta:
        model = Equipment
        fields = '__all__'
