from django_extended.serializers.fields import EnumField
from rest_framework import serializers

from metadatax.equipment.models import HydrophoneDirectivity, HydrophoneSpecification


class HydrophoneSpecificationSerializer(serializers.ModelSerializer):
    directivity = EnumField(HydrophoneDirectivity)

    class Meta:
        model = HydrophoneSpecification
        fields = "__all__"
