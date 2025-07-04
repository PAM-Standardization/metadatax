from rest_framework import serializers

from metadatax.ontology.models import Sound


class SoundSerializer(serializers.ModelSerializer):
    """Sound Serializer"""

    class Meta:
        model = Sound
        fields = "__all__"
