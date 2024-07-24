from rest_framework import serializers
from metadatax.models.acquisition import (
    Institution,
    Project,
    Deployment,
    ChannelConfiguration,
    Platform,
    Accessibility,
    Campaign,
    Site,
)
from metadatax.serializers.utils import EnumField


class ChannelConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelConfiguration
        fields = "__all__"
        depth = 3


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = "__all__"
        depth = 1


class ProjectSerializer(serializers.ModelSerializer):
    accessibility = EnumField(enum=Accessibility)

    class Meta:
        model = Project
        fields = "__all__"
        depth = 1


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        exclude = [
            "project",
        ]
        depth = 1


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        exclude = [
            "project",
        ]
        depth = 1


class ChannelConfigurationWithoutDeploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelConfiguration
        exclude = [
            "deployment",
        ]
        depth = 2


class DeploymentWithoutProjectSerializer(serializers.ModelSerializer):
    platform = PlatformSerializer()
    name = serializers.CharField(source="__str__")
    channels = ChannelConfigurationSerializer(
        source="channelconfiguration_set",
        many=True,
    )

    class Meta:
        model = Deployment
        exclude = [
            "project",
        ]
        depth = 1


class ProjectFullSerializer(serializers.ModelSerializer):
    accessibility = EnumField(enum=Accessibility)
    campaigns = CampaignSerializer(many=True)
    sites = SiteSerializer(many=True)
    deployments = DeploymentWithoutProjectSerializer(many=True)

    class Meta:
        model = Project
        fields = "__all__"
        depth = 1


class DeploymentSerializer(serializers.ModelSerializer):
    platform = PlatformSerializer()
    project = ProjectSerializer()
    name = serializers.CharField(source="__str__")
    channel = ChannelConfigurationSerializer(
        source="channelconfiguration_set", many=True
    )

    class Meta:
        model = Deployment
        fields = "__all__"
        depth = 1


class DeploymentLightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deployment
        fields = "__all__"


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = "__all__"
