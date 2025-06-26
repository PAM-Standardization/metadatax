from rest_framework import serializers

from metadatax_acquisition.models import DeploymentMobilePosition


class DeploymentMobilePositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeploymentMobilePosition
        fields = "__all__"
