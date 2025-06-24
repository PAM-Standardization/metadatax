from rest_framework import serializers

from metadatax_ontology.models import PhysicalDescriptor, SignalShape, SignalPlurality
from utils.serializers import EnumField


class PhysicalDescriptorSerializer(serializers.ModelSerializer):
    """PhysicalDescriptor Serializer"""

    shape = EnumField(SignalShape)
    plurality = EnumField(SignalPlurality)

    class Meta:
        model = PhysicalDescriptor
        fields = "__all__"
        exclude = [
            "label",
        ]
