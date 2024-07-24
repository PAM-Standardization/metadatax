from rest_framework import serializers
from metadatax.models.equipment import Recorder, Hydrophone


class RecorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recorder
        fields = "__all__"


class HydrophoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hydrophone
        fields = "__all__"
