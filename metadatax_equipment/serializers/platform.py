from rest_framework import serializers

from metadatax_common.serializers import ContactSerializer
from metadatax_equipment.models import Platform
from .platform_type import PlatformTypeSerializer


class PlatformSerializer(serializers.ModelSerializer):
    owner = ContactSerializer()
    provider = ContactSerializer()
    type = PlatformTypeSerializer()

    # TODO: add mobile platforms points

    class Meta:
        model = Platform
        fields = '__all__'
