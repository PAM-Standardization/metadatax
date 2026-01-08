from rest_framework import serializers

from metadatax.acquisition.models import ChannelConfiguration
from metadatax.equipment.serializers import EquipmentSerializer
from .channel_configuration_specifications import (
    ChannelConfigurationDetectorSpecificationSerializer,
    ChannelConfigurationRecorderSpecificationSerializer,
)


class ChannelConfigurationSerializer(serializers.ModelSerializer):
    recorder_specification = ChannelConfigurationRecorderSpecificationSerializer()
    detector_specification = ChannelConfigurationDetectorSpecificationSerializer()
    storages = EquipmentSerializer(many=True)

    class Meta:
        model = ChannelConfiguration
        exclude = [
            "files",
        ]
