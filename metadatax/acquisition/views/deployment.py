"""Acquisition models for metadata app"""
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.acquisition.models import Deployment
from metadatax.acquisition.serializers import DeploymentSerializer


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
    search_fields = [
        "name",
        "project__name",
        "project__accessibility",
        "site__name",
        "campaign__name",
        "platform__name",
        "platform__type__name",
        "deployment_vessel",
        "recovery_vessel",
        "contacts__role",
        "contacts__contact__name",
        "contacts__contact__mail",
    ]
