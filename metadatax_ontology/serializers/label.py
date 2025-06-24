from rest_framework import serializers

from metadatax_ontology.models import Label
from metadatax_ontology.serializers.physical_descriptor import (
    PhysicalDescriptorSerializer,
)
from metadatax_ontology.serializers.sound import SoundSerializer
from metadatax_ontology.serializers.source import SourceSerializer


class LabelSerializer(serializers.ModelSerializer):
    source = SourceSerializer()
    sound = SoundSerializer(allow_null=True)
    physical_descriptor = PhysicalDescriptorSerializer(allow_null=True)

    class Meta:
        model = Label
        fields = "__all__"
