from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.acquisition.models import DeploymentMobilePosition
from metadatax.acquisition.serializers import DeploymentMobilePositionSerializer


class DeploymentMobilePositionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DeploymentMobilePosition.objects.all()
    serializer_class = DeploymentMobilePositionSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    search_fields = [
        "deployment__name",
        "deployment__project__name",
        "deployment__project__accessibility",
        "deployment__site__name",
        "deployment__campaign__name",
        "deployment__platform__name",
        "deployment__platform__type__name",
    ]
