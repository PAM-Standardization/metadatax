from rest_framework import serializers

from metadatax.ontology.models import Source


class SourceSerializer(serializers.ModelSerializer):
    """Source Serializer"""

    related_bibliography = serializers.PrimaryKeyRelatedField(
        read_only=True,
        many=True,
    )

    class Meta:
        model = Source
        fields = "__all__"
