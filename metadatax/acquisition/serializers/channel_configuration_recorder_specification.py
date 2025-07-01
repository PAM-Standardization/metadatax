from rest_framework import serializers

from metadatax.acquisition.models import ChannelConfigurationRecorderSpecification
from metadatax.data.models import FileFormat
from metadatax.equipment.serializers import EquipmentSerializer


class ChannelConfigurationRecorderSpecificationSerializer(serializers.ModelSerializer):
    recorder = EquipmentSerializer()
    hydrophone = EquipmentSerializer()
    recording_formats = serializers.SlugRelatedField(
        slug_field="name",
        queryset=FileFormat.objects.all(),
        many=True,
    )

    class Meta:
        model = ChannelConfigurationRecorderSpecification
        fields = "__all__"
