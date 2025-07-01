from rest_framework import serializers

from metadatax.acquisition.models import Project, Financing
from metadatax.common.models import Accessibility
from metadatax.common.serializers import ContactRoleSerializer
from metadatax.utils import EnumField
from .campaign import CampaignSerializer
from .deployment import DeploymentExportSerializer
from .project_type import ProjectTypeSerializer
from .site import SiteSerializer


class ProjectSerializer(serializers.ModelSerializer):
    accessibility = EnumField(enum=Accessibility)
    financing = EnumField(enum=Financing)
    contacts = ContactRoleSerializer(many=True)
    project_type = ProjectTypeSerializer()

    class Meta:
        model = Project
        fields = "__all__"


class ProjectExportSerializer(ProjectSerializer):
    campaigns = CampaignSerializer(many=True)
    sites = SiteSerializer(many=True)
    deployments = DeploymentExportSerializer(many=True)

    class Meta:
        model = Project
        fields = "__all__"
