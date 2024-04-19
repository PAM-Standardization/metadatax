from rest_framework import  serializers
from metadatax.models.acquisition import Institution, Project, Deployment, ChannelConfiguration

InstitutionFields = [
    "name" ,
    "contact"
]

ProjectFields = [
    "name",
    "responsible_parties" ,
    "accessibility" ,
    "doi",
    "project_type",
    "project_goal"
]

DeploymentFields = [
"project",
"provider",
"campaign",
"name",
"deployment_date",
"deployment_vessel",
"recovery_date",
"recovery_vessel",
"description",
"platform_type",
"platform_description",
"platform_name",
"longitude",
"latitude",
"bathymetric_depth"
]


ChannelConfigurationFields = [
"deployment",
"hydrophone",
"recorder",
"channel_name",
"gain",
"hydrophone_depth",
"continuous",
"duty_cycle_on",
"duty_cycle_off",
"sampling_frequency",
"recording_format",
"sample_depth"
]

class ChannelConfigurationAPIParametersSerializer(serializers.Serializer):
    channel_name = serializers.CharField(help_text="Name of the channel")

class CreateChannelConfigurationAPIParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelConfiguration
        fields = ChannelConfigurationFields


class DeploymentAPIParametersSerializer(serializers.Serializer):
    deployment_name = serializers.CharField(help_text="Name of the deployment")

class CreateDeploymentAPIParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deployment
        fields = DeploymentFields

class ProjectAPIParametersSerializer(serializers.Serializer):
    project_name = serializers.CharField(help_text="Name of the project")


class CreateProjectAPIParametersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ProjectFields

class InstitutionAPIParametersSerializer(serializers.Serializer):
    institution_name = serializers.CharField(help_text="Name of the institution")

class CreateInstitutionAPIParametersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institution
        fields = InstitutionFields




