"""File Serializers for metadata app"""

from rest_framework import serializers
from metadatax.models.data import File


class FileSerializer(serializers.Serializer):
    class Meta:
        model = File
        fields = "__all__"
