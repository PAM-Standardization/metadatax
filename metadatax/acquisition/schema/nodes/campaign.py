from django_extension.schema.interfaces import ExtendedInterface
from django_extension.schema.types import ExtendedNode

from metadatax.acquisition.models import Campaign


class CampaignNode(ExtendedNode):
    class Meta:
        model = Campaign
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
            "project_id": ["exact", "in"],
        }
