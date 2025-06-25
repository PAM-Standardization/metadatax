from rest_framework import serializers

from metadatax_acquisition.models import ChannelConfiguration
from metadatax_equipment.serializers import EquipmentSerializer
from .channel_configuration_detector_specification import (
    ChannelConfigurationDetectorSpecificationSerializer,
)
from .channel_configuration_recorder_specification import (
    ChannelConfigurationRecorderSpecificationSerializer,
)


class ChannelConfigurationSerializer(serializers.ModelSerializer):
    recorder_specification = ChannelConfigurationRecorderSpecificationSerializer()
    detector_specification = ChannelConfigurationDetectorSpecificationSerializer()
    other_equipments = EquipmentSerializer(many=True)

    class Meta:
        model = ChannelConfiguration
        fields = "__all__"
