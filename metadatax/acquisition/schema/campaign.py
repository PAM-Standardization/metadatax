from django_filters import FilterSet, NumberFilter
from graphene import ID, relay

from metadatax.acquisition.models import Campaign
from metadatax.utils.schema import MxObjectType


class CampaignFilter(FilterSet):
    deployments__id = NumberFilter()

    class Meta:
        model = Campaign
        fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
            "project_id": ["exact", "in"],
            "deployments__id": ["exact", "in"],
        }


class CampaignNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = Campaign
        fields = "__all__"
        filterset_class = CampaignFilter
        interfaces = (relay.Node,)
