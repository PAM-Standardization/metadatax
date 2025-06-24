from rest_framework import serializers

from metadatax.models.equipment import (
    Recorder,
    Hydrophone,
    HydrophoneModel,
    HydrophoneDirectivity,
)
from utils.serializers import EnumField


class RecorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recorder
        fields = "__all__"
        depth = 2


class HydrophoneModelSerializer(serializers.ModelSerializer):
    directivity = EnumField(enum=HydrophoneDirectivity)

    class Meta:
        model = HydrophoneModel
        fields = "__all__"
        depth = 1


class HydrophoneSerializer(serializers.ModelSerializer):
    model = HydrophoneModelSerializer()

    class Meta:
        model = Hydrophone
        fields = "__all__"
