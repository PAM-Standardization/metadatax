from rest_framework import serializers

from metadatax_acquisition.models import ChannelConfigurationRecorderSpecification
from metadatax_data.models import FileFormat
from metadatax_equipment.serializers import EquipmentSerializer


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
