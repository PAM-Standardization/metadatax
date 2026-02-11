import graphene
from django_extension.schema.types import ExtendedNode

from metadatax.acquisition.models import Deployment
from metadatax.common.schema import ContactRelationNode

from .deployment_mobile_position import DeploymentMobilePositionNode


class DeploymentNode(ExtendedNode):
    mobile_positions = graphene.List(DeploymentMobilePositionNode)

    contacts = graphene.List(ContactRelationNode)

    class Meta:
        model = Deployment
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "project_id": ["exact", "in"],
            "site_id": ["exact", "in"],
            "campaign_id": ["exact", "in"],
            "platform_id": ["exact", "in"],
            "longitude": ["exact", "lt", "lte", "gt", "gte"],
            "latitude": ["exact", "lt", "lte", "gt", "gte"],
            "name": ["exact", "icontains"],
            "bathymetric_depth": ["exact", "lt", "lte", "gt", "gte"],
            "deployment_date": ["exact", "lt", "lte", "gt", "gte"],
            "deployment_vessel": ["exact", "icontains"],
            "recovery_date": ["exact", "lt", "lte", "gt", "gte"],
            "recovery_vessel": ["exact", "icontains"],
            "description": ["icontains"],
        }

    def resolve_contacts(self: Deployment, info):
        return self.contacts.all()
