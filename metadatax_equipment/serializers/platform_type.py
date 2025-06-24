from rest_framework import serializers

from metadatax_equipment.models import PlatformType


class PlatformTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformType
        fields = '__all__'
