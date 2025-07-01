from rest_framework import serializers

from metadatax.common.serializers import ContactSerializer
from metadatax.equipment.models import Platform
from .platform_type import PlatformTypeSerializer


class PlatformSerializer(serializers.ModelSerializer):
    owner = ContactSerializer()
    provider = ContactSerializer()
    type = PlatformTypeSerializer()
    
    class Meta:
        model = Platform
        fields = '__all__'
