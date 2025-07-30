from django_filters import FilterSet, NumberFilter
from graphene import ID, relay

from metadatax.acquisition.models import Deployment
from metadatax.utils.schema import MxObjectType


class DeploymentFilter(FilterSet):
    contacts__id = NumberFilter()
    channel_configurations__id = NumberFilter()
    mobile_positions__id = NumberFilter()

    class Meta:
        model = Deployment
        fields = {
            "id": ["exact", "in"],
            "project_id": ["exact", "in"],
            "site_id": ["exact", "in"],
            "campaign_id": ["exact", "in"],
            "platform_id": ["exact", "in"],
            "contacts__id": ["exact", "in"],
            "mobile_positions__id": ["exact", "in"],
            "channel_configurations__id": ["exact", "in"],
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


class DeploymentNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = Deployment
        fields = "__all__"
        filterset_class = DeploymentFilter
        interfaces = (relay.Node,)
