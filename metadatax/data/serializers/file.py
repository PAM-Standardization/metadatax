from rest_framework import serializers

from metadatax.data.models import FileFormat, File
from .audio_properties import AudioPropertiesSerializer
from .detection_properties import DetectionPropertiesSerializer


class FileSerializer(serializers.ModelSerializer):

    format = serializers.SlugRelatedField(
        slug_field="name", queryset=FileFormat.objects.all()
    )
    audio_properties = AudioPropertiesSerializer(required=False)
    detection_properties = DetectionPropertiesSerializer(required=False)

    class Meta:
        model = File
        fields = "__all__"
