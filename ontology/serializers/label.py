from rest_framework import serializers

from ontology.models import Label
from ontology.serializers.physical_descriptor import PhysicalDescriptorSerializer
from ontology.serializers.sound import SoundSerializer
from ontology.serializers.source import SourceSerializer


class LabelSerializer(serializers.ModelSerializer):
    source = SourceSerializer()
    sound = SoundSerializer(allow_null=True)
    physical_descriptor = PhysicalDescriptorSerializer(allow_null=True)

    class Meta:
        model = Label
        fields = "__all__"
