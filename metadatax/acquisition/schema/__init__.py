import graphene
from graphene import ObjectType, Field
from graphene_django_pagination import DjangoPaginationConnectionField

from metadatax.acquisition.models import (
    Campaign,
    Site,
    Project,
    ChannelConfiguration,
    ChannelConfigurationRecorderSpecification,
    ChannelConfigurationDetectorSpecification,
    Deployment,
    DeploymentMobilePosition,
    ProjectType,
)
from .campaign import CampaignNode
from .channel_configuration import ChannelConfigurationNode
from .channel_configuration_detector_specification import (
    ChannelConfigurationDetectorSpecificationNode,
)
from .channel_configuration_recorder_specification import (
    ChannelConfigurationRecorderSpecificationFilter,
    ChannelConfigurationRecorderSpecificationNode,
)
from .deployment import DeploymentNode
from .deployment_mobile_position import DeploymentMobilePositionNode
from .project import ProjectNode
from .project_type import ProjectTypeNode
from .site import SiteNode


class AcquisitionQuery(ObjectType):
    all_campaigns = DjangoPaginationConnectionField(CampaignNode)
    campaign_by_id = Field(CampaignNode, id=graphene.ID(required=True))

    all_channel_configurations = DjangoPaginationConnectionField(
        ChannelConfigurationNode
    )
    channel_configuration_by_id = Field(
        ChannelConfigurationNode, id=graphene.ID(required=True)
    )

    all_channel_configurations_detector_specifications = (
        DjangoPaginationConnectionField(ChannelConfigurationDetectorSpecificationNode)
    )
    channel_configuration_detector_specification_by_id = Field(
        ChannelConfigurationDetectorSpecificationNode, id=graphene.ID(required=True)
    )

    all_channel_configurations_recorder_specifications = (
        DjangoPaginationConnectionField(ChannelConfigurationRecorderSpecificationNode)
    )
    channel_configuration_recorder_specification_by_id = Field(
        ChannelConfigurationRecorderSpecificationNode, id=graphene.ID(required=True)
    )

    all_deployments = DjangoPaginationConnectionField(DeploymentNode)
    deployment_by_id = Field(DeploymentNode, id=graphene.ID(required=True))

    all_deployment_mobile_positions = DjangoPaginationConnectionField(
        DeploymentMobilePositionNode
    )
    deployment_mobile_position_by_id = Field(
        DeploymentMobilePositionNode, id=graphene.ID(required=True)
    )

    all_projects = DjangoPaginationConnectionField(ProjectNode)
    project_by_id = Field(ProjectNode, id=graphene.ID(required=True))

    all_project_types = DjangoPaginationConnectionField(ProjectTypeNode)
    project_type_by_id = Field(ProjectTypeNode, id=graphene.ID(required=True))

    all_sites = DjangoPaginationConnectionField(SiteNode)
    site_by_id = Field(SiteNode, id=graphene.ID(required=True))

    def resolve_campaign_by_id(self, info, id: int):
        return Campaign.objects.get(pk=id)

    def resolve_channel_configuration_by_id(self, info, id: int):
        return ChannelConfiguration.objects.get(pk=id)

    def resolve_channel_configuration_detector_specification_by_id(self, info, id: int):
        return ChannelConfigurationDetectorSpecification.objects.get(pk=id)

    def resolve_channel_configuration_recorder_specification_by_id(self, info, id: int):
        return ChannelConfigurationRecorderSpecification.objects.get(pk=id)

    def resolve_project_by_id(self, info, id: int):
        return Project.objects.get(pk=id)

    def resolve_project_type_by_id(self, info, id: int):
        return ProjectType.objects.get(pk=id)

    def resolve_deployment_by_id(self, info, id: int):
        return Deployment.objects.get(pk=id)

    def resolve_deployment_mobile_position_by_id(self, info, id: int):
        return DeploymentMobilePosition.objects.get(pk=id)

    def resolve_site_by_id(self, info, id: int):
        return Site.objects.get(pk=id)
