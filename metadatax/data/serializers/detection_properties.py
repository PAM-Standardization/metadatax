from rest_framework import serializers

from metadatax.data.models import DetectionProperties


class DetectionPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetectionProperties
        fields = "__all__"
