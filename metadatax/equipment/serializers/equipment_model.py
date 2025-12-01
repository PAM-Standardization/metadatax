from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from metadatax.common.serializers import InstitutionSerializer
from metadatax.equipment.models import EquipmentModel, EquipmentModelSpecification
from .acoustic_detector_specification import AcousticDetectorSpecificationSerializer
from .hydrophone_specification import HydrophoneSpecificationSerializer
from .recorder_specification import RecorderSpecificationSerializer
from .storage_specification import StorageSpecificationSerializer


class EquipmentModelSpecificationSerializer(serializers.ModelSerializer):
    specification = serializers.SerializerMethodField()
    specification_type = serializers.SlugRelatedField('model', queryset=ContentType.objects.all())

    class Meta:
        model = EquipmentModelSpecification
        exclude = ('model', 'specification_id')

    def get_specification(self, obj: EquipmentModelSpecification):
        """
        Serialize the related object based on its type
        """
        if obj.specification is None:
            return None

        # Map content types to their serializers
        serializer_map = {
            'acousticdetectorspecification': AcousticDetectorSpecificationSerializer,
            'hydrophonespecification': HydrophoneSpecificationSerializer,
            'recorderspecification': RecorderSpecificationSerializer,
            'storagespecification': StorageSpecificationSerializer,
        }

        model_name = obj.specification_type.model
        serializer_class = serializer_map.get(str(model_name))

        if serializer_class:
            return serializer_class(obj.specification).data

        # Fallback: return basic representation
        return {'id': obj.specification_id}


class EquipmentModelSerializer(serializers.ModelSerializer):
    provider = InstitutionSerializer()
    specification_relations = EquipmentModelSpecificationSerializer(many=True)

    class Meta:
        model = EquipmentModel
        fields = "__all__"
