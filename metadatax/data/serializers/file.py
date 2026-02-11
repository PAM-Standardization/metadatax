from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from metadatax.data.models import FileFormat, File
from metadatax.data.serializers import AudioPropertiesSerializer, DetectionPropertiesSerializer


class FileSerializer(serializers.ModelSerializer):
    format = serializers.SlugRelatedField(
        slug_field="name", queryset=FileFormat.objects.all()
    )
    property = serializers.SerializerMethodField()
    property_type = serializers.SlugRelatedField('model', queryset=ContentType.objects.all())

    class Meta:
        model = File
        exclude = (
            "property_id"
        )

    def get_property(self, obj: File):
        """
        Serialize the related object based on its type
        """
        if obj.property is None:
            return None

        # Map content types to their serializers
        serializer_map = {
            'audioproperties': AudioPropertiesSerializer,
            'detectionproperties': DetectionPropertiesSerializer,
        }

        model_name = obj.property_type.model
        serializer_class = serializer_map.get(str(model_name))

        if serializer_class:
            return serializer_class(obj.property).data

        # Fallback: return basic representation
        return {'id': obj.property_id}
