from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax_acquisition.models import DeploymentMobilePosition
from metadatax_acquisition.serializers import DeploymentMobilePositionSerializer


class DeploymentMobilePositionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DeploymentMobilePosition.objects.all()
    serializer_class = DeploymentMobilePositionSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
