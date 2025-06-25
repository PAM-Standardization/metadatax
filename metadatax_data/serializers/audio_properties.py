from rest_framework import serializers

from metadatax_data.models import AudioProperties


class AudioPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioProperties
        fields = "__all__"
