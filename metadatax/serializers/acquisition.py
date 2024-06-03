from rest_framework import serializers
from metadatax.models.acquisition import (
    Institution,
    Project,
    Deployment,
    ChannelConfiguration, Platform, Accessibility
)
from metadatax.serializers.utils import EnumField


class ChannelConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelConfiguration
        fields = '__all__'
        depth = 2

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'
        depth = 1


class ProjectSerializer(serializers.ModelSerializer):
    accessibility = EnumField(enum=Accessibility)

    class Meta:
        model = Project
        fields = '__all__'
        depth = 1


class DeploymentSerializer(serializers.ModelSerializer):
    platform = PlatformSerializer()
    project = ProjectSerializer()
    name = serializers.CharField(source="__str__")

    class Meta:
        model = Deployment
        fields = '__all__'
        depth = 1


class DeploymentLightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deployment
        fields = '__all__'


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'
