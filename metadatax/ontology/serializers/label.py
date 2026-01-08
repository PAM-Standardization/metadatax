from django_extended.serializers.fields import EnumField
from rest_framework import serializers

from metadatax.ontology.models import Label, SignalShape, SignalPlurality
from metadatax.ontology.serializers.sound import SoundSerializer
from metadatax.ontology.serializers.source import SourceSerializer


class LabelSerializer(serializers.ModelSerializer):
    source = SourceSerializer()
    sound = SoundSerializer(allow_null=True)

    shape = EnumField(SignalShape)
    plurality = EnumField(SignalPlurality)

    class Meta:
        model = Label
        fields = "__all__"
