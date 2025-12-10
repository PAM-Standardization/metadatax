from rest_framework import serializers

from metadatax.data.models import FileFormat, DetectionFile
from .detection_properties import DetectionPropertiesSerializer


class DetectionFileSerializer(serializers.ModelSerializer):
    format = serializers.SlugRelatedField(
        slug_field="name", queryset=FileFormat.objects.all()
    )
    detection_properties = DetectionPropertiesSerializer(required=False)

    class Meta:
        model = DetectionFile
        fields = "__all__"
