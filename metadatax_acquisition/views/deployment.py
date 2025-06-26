"""Acquisition models for metadata app"""
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax_acquisition.models import Deployment
from metadatax_acquisition.serializers import DeploymentSerializer


class DeploymentViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = Deployment.objects.select_related(
        "campaign",
        "site",
        "platform",
        "platform__type",
    ).prefetch_related(
        "contacts",
    )
    serializer_class = DeploymentSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
