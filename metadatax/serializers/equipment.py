from rest_framework import serializers, filters
from metadatax.models.equipment import Recorder, Hydrophone

RecorderFields = [
"provider",
"model",
"serial_number",
"number_of_channels"
]
HydrophoneFields = [
    "provider",
    "model",
    "serial_number",
    "sensitivity",
    "directivity",
    "bandwidth",
    "noise_floor",
    "dynamic_range",
    "max_operating_depth",
    "operating_min_temperature",
    "operating_max_temperature",
]

class RecorderAPIParametersSerializer(serializers.Serializer):
        recorder_provider_name = serializers.CharField(help_text="Provider of recorder")


class CreateRecorderAPIParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recorder
        fields = RecorderFields

class HydrophoneAPIParametersSerializer(serializers.Serializer):
    hydrophone_provider_name = serializers.CharField(help_text="Provider of hydrophone")

class CreateHydrophoneAPIParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hydrophone
        fields = HydrophoneFields