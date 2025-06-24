from rest_framework import serializers

from metadatax_acquisition.models.deployment import Deployment
from metadatax_common.serializers import ContactSerializer
from metadatax_equipment.serializers import PlatformSerializer
from .campaign import CampaignSerializer
from .site import SiteSerializer


class DeploymentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="__str__")
    site = SiteSerializer(required=False)
    campaign = CampaignSerializer(required=False)
    platform = PlatformSerializer()
    contacts = ContactSerializer(many=True)

    class Meta:
        model = Deployment
        fields = "__all__"


class DeploymentExportSerializer(DeploymentSerializer):
    # TODO: add channel configurations

    class Meta:
        model = Deployment
        fields = "__all__"
