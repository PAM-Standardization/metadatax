from rest_framework import serializers

from metadatax.common.serializers import InstitutionSerializer
from metadatax.equipment.models import Platform
from .platform_type import PlatformTypeSerializer


class PlatformSerializer(serializers.ModelSerializer):
    owner = InstitutionSerializer()
    provider = InstitutionSerializer()

    type = PlatformTypeSerializer()

    class Meta:
        model = Platform
        fields = "__all__"
