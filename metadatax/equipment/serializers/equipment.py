from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from metadatax.equipment.models import Equipment
from .equipment_model import EquipmentModelSerializer
from ...common.serializers import PersonSerializer, TeamSerializer, InstitutionSerializer


class EquipmentSerializer(serializers.ModelSerializer):
    model = EquipmentModelSerializer()

    owner = serializers.SerializerMethodField()
    owner_type = serializers.SlugRelatedField('model', queryset=ContentType.objects.all())

    class Meta:
        model = Equipment
        fields = "__all__"

    def get_owner(self, obj: Equipment):
        """
        Serialize the related object based on its type
        """
        if obj.owner is None:
            return None

        # Map content types to their serializers
        serializer_map = {
            'person': PersonSerializer,
            'team': TeamSerializer,
            'institution': InstitutionSerializer,
        }

        model_name = obj.owner_type.model
        serializer_class = serializer_map.get(str(model_name))

        if serializer_class:
            return serializer_class(obj.owner).data

        # Fallback: return basic representation
        return {'id': obj.owner_id}
