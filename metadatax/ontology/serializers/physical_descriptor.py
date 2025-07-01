from rest_framework import serializers

from metadatax.ontology.models import PhysicalDescriptor, SignalShape, SignalPlurality
from metadatax.utils import EnumField


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
