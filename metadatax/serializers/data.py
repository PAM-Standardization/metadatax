"""File Serializers for metadata app"""

from rest_framework import serializers

class AudioSerializer(serializers.Serializer):
    file = serializers.FileField()


class DataAPIParametersSerializer(serializers.Serializer):
    name = serializers.CharField(help_text="Name of the sample")