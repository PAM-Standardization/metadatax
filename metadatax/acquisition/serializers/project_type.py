from rest_framework import serializers

from metadatax.acquisition.models import ProjectType


class ProjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectType
        fields = "__all__"
