from rest_framework import serializers

from metadatax_acquisition.models.deployment import Deployment
from metadatax_common.serializers import ContactRoleSerializer
from metadatax_equipment.serializers import PlatformSerializer
from .campaign import CampaignSerializer
from .channel_configuration import ChannelConfigurationSerializer
from .deployment_mobile_position import DeploymentMobilePositionSerializer
from .site import SiteSerializer


class DeploymentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="__str__")
    site = SiteSerializer(required=False)
    campaign = CampaignSerializer(required=False)
    platform = PlatformSerializer()
    contacts = ContactRoleSerializer(many=True)

    class Meta:
        model = Deployment
        fields = "__all__"


class DeploymentExportSerializer(DeploymentSerializer):
    channel_configurations = ChannelConfigurationSerializer(many=True)
    mobile_positions = DeploymentMobilePositionSerializer(many=True)

    class Meta:
        model = Deployment
        fields = "__all__"
