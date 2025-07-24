from rest_framework import serializers

from metadatax.equipment.models import PlatformType


class PlatformTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformType
        fields = "__all__"
