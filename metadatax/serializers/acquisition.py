from rest_framework import serializers
from metadatax.models.acquisition import (
    Institution,
    Project,
    Deployment,
    ChannelConfiguration
)


class ChannelConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelConfiguration
        fields = '__all__'


class DeploymentSerializer(serializers.ModelSerializer):
    provider = serializers.CharField(source='provider.name', allow_null=True)
    project = serializers.CharField(source='project.name')
    class Meta:
        model = Deployment
        fields = '__all__'


class DeploymentLightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deployment
        fields = '__all__'

class DeploymentGlobalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deployment
        fields = '__all__'
        depth = 2

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'


class ProjectAPIParametersSerializer(serializers.Serializer):
    project_name = serializers.CharField(help_text="Name of the project")


class CreateProjectAPIParametersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = [
            "name",
            "responsible_parties" ,
            "accessibility" ,
            "doi",
            "project_type",
            "project_goal"
        ]


