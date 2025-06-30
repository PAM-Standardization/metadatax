from rest_framework import serializers

from metadatax.equipment.models import MaintenanceType


class MaintenanceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceType
        fields = '__all__'
