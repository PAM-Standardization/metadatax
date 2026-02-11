from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from metadatax.common.serializers import InstitutionSerializer, PersonSerializer, TeamSerializer
from metadatax.equipment.models import Platform
from .platform_type import PlatformTypeSerializer


class PlatformSerializer(serializers.ModelSerializer):
    provider = InstitutionSerializer()

    type = PlatformTypeSerializer()

    owner = serializers.SerializerMethodField()
    owner_type = serializers.SlugRelatedField('model', queryset=ContentType.objects.all())

    class Meta:
        model = Platform
        fields = "__all__"

    def get_owner(self, obj: Platform):
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
