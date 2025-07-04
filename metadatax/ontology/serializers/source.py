from rest_framework import serializers

from metadatax.ontology.models import Source


class SourceSerializer(serializers.ModelSerializer):
    """Source Serializer"""

    class Meta:
        model = Source
        fields = "__all__"
