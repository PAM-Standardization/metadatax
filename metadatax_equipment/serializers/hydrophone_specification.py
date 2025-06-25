from rest_framework import serializers

from metadatax_equipment.models import HydrophoneDirectivity, HydrophoneSpecification
from utils.serializers import EnumField


class HydrophoneSpecificationSerializer(serializers.ModelSerializer):
    directivity = EnumField(HydrophoneDirectivity)

    class Meta:
        model = HydrophoneSpecification
        fields = '__all__'
