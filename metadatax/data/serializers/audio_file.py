from rest_framework import serializers

from metadatax.data.models import FileFormat, AudioFile
from .audio_properties import AudioPropertiesSerializer


class AudioFileSerializer(serializers.ModelSerializer):
    format = serializers.SlugRelatedField(
        slug_field="name", queryset=FileFormat.objects.all()
    )
    audio_properties = AudioPropertiesSerializer(required=False)

    class Meta:
        model = AudioFile
        fields = "__all__"
