from django_extension.serializers import EnumField
from rest_framework import serializers

from metadatax.acquisition.models import ChannelConfiguration, ChannelConfigurationStatus
from metadatax.equipment.serializers import EquipmentSerializer
from .channel_configuration_specifications import (
    ChannelConfigurationDetectorSpecificationSerializer,
    ChannelConfigurationRecorderSpecificationSerializer,
)


class ChannelConfigurationSerializer(serializers.ModelSerializer):
    recorder_specification = ChannelConfigurationRecorderSpecificationSerializer()
    detector_specification = ChannelConfigurationDetectorSpecificationSerializer()
    storages = EquipmentSerializer(many=True)
    status = EnumField(enum=ChannelConfigurationStatus)

    class Meta:
        model = ChannelConfiguration
        exclude = [
            "files",
        ]
