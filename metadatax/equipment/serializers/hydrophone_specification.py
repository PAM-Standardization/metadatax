from rest_framework import serializers

from metadatax.equipment.models import HydrophoneDirectivity, HydrophoneSpecification
from metadatax.utils import EnumField


class HydrophoneSpecificationSerializer(serializers.ModelSerializer):
    directivity = EnumField(HydrophoneDirectivity)

    class Meta:
        model = HydrophoneSpecification
        fields = "__all__"
