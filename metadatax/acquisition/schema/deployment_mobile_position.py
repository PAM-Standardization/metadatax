from django_filters import FilterSet
from graphene import ID, relay

from metadatax.acquisition.models import DeploymentMobilePosition
from metadatax.utils.schema import MxObjectType


class DeploymentMobilePositionFilter(FilterSet):
    class Meta:
        model = DeploymentMobilePosition
        fields = {
            "id": ["exact", "in"],
            "deployment_id": ["exact", "in"],
            "datetime": ["exact", "lt", "lte", "gt", "gte"],
            "longitude": ["exact", "lt", "lte", "gt", "gte"],
            "latitude": ["exact", "lt", "lte", "gt", "gte"],
            "depth": ["exact", "lt", "lte", "gt", "gte"],
            "heading": ["exact", "lt", "lte", "gt", "gte"],
            "pitch": ["exact", "lt", "lte", "gt", "gte"],
            "roll": ["exact", "lt", "lte", "gt", "gte"],
        }


class DeploymentMobilePositionNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = DeploymentMobilePosition
        fields = "__all__"
        filterset_class = DeploymentMobilePositionFilter
        interfaces = (relay.Node,)
