from rest_framework import serializers

from metadatax.ontology.models import Sound


class SoundSerializer(serializers.ModelSerializer):
    """Sound Serializer"""

    related_bibliography = serializers.PrimaryKeyRelatedField(
        read_only=True,
        many=True,
    )

    class Meta:
        model = Sound
        fields = "__all__"
