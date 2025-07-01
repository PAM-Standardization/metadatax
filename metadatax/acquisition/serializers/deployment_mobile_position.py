from rest_framework import serializers

from metadatax.acquisition.models import DeploymentMobilePosition


class DeploymentMobilePositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeploymentMobilePosition
        fields = "__all__"
