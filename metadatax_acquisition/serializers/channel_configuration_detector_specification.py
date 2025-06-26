from rest_framework import serializers

from metadatax_acquisition.models import ChannelConfigurationDetectorSpecification
from metadatax_data.models import FileFormat
from metadatax_equipment.serializers import EquipmentSerializer
from metadatax_ontology.serializers import LabelSerializer


class ChannelConfigurationDetectorSpecificationSerializer(serializers.ModelSerializer):
    detector = EquipmentSerializer()
    output_formats = serializers.SlugRelatedField(
        slug_field="name",
        queryset=FileFormat.objects.all(),
        many=True,
    )
    labels = LabelSerializer(many=True)

    class Meta:
        model = ChannelConfigurationDetectorSpecification
        fields = "__all__"
