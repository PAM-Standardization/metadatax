from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax_acquisition.models import Campaign
from metadatax_acquisition.serializers import CampaignSerializer


class CampaignViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
