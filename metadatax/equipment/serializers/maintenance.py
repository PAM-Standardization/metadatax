from rest_framework import serializers

from metadatax.common.serializers import ContactSerializer, InstitutionSerializer
from metadatax.equipment.models import Maintenance
from .maintenance_type import MaintenanceTypeSerializer


class MaintenanceSerializer(serializers.ModelSerializer):
    type = MaintenanceTypeSerializer(read_only=True)
    maintainer = ContactSerializer()
    maintainer_institution = InstitutionSerializer()

    class Meta:
        model = Maintenance
        exclude = ['platform', 'equipment']
