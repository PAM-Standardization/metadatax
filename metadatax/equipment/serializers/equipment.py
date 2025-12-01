from rest_framework import serializers

from metadatax.common.serializers import InstitutionSerializer
from metadatax.equipment.models import Equipment
from .equipment_model import EquipmentModelSerializer


class EquipmentSerializer(serializers.ModelSerializer):
    owner = InstitutionSerializer()

    model = EquipmentModelSerializer()

    class Meta:
        model = Equipment
        fields = "__all__"
