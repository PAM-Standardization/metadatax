from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.acquisition.models import Campaign
from metadatax.acquisition.serializers import CampaignSerializer


class CampaignViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    search_fields = ["name", "project__name"]
