from django_extended.schema.fields import ByIdField
from graphene import ObjectType
from graphene_django_pagination import DjangoPaginationConnectionField

from .nodes import *


class AcquisitionQuery(ObjectType):
    # Project
    all_projects = DjangoPaginationConnectionField(ProjectNode)
    project_by_id = ByIdField(ProjectNode)
    all_project_types = DjangoPaginationConnectionField(ProjectTypeNode)

    # Site
    all_sites = DjangoPaginationConnectionField(SiteNode)
    site_by_id = ByIdField(SiteNode)

    # Campaign
    all_campaigns = DjangoPaginationConnectionField(CampaignNode)
    campaign_by_id = ByIdField(CampaignNode)

    # Deployment
    all_deployments = DjangoPaginationConnectionField(DeploymentNode)
    deployment_by_id = ByIdField(DeploymentNode)

    # Channel Configuration
    all_channel_configurations = DjangoPaginationConnectionField(ChannelConfigurationNode)
    channel_configuration_by_id = ByIdField(ChannelConfigurationNode)
