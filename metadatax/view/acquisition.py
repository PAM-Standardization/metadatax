"""Acquisition models for metadata app"""
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.models.acquisition import (
    ChannelConfiguration,
    Deployment,
    Project,
    Institution,
)
from metadatax.serializers.acquisition import (
    InstitutionSerializer,
    ProjectSerializer,
    DeploymentSerializerWithChannel,
    ChannelConfigurationSerializer,
)


class InstitutionViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]


class ProjectViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = Project.objects.select_related("project_type").prefetch_related(
        "responsible_parties",
    )
    serializer_class = ProjectSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]


class DeploymentViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = Deployment.objects.select_related(
        "project",
        "project__project_type",
        "provider",
        "campaign",
        "site",
        "platform",
        "platform__type",
    ).prefetch_related(
        "project__responsible_parties",
        "channelconfiguration_set",
        "channelconfiguration_set__hydrophone",
        "channelconfiguration_set__hydrophone__model",
        "channelconfiguration_set__hydrophone__model__provider",
        "channelconfiguration_set__recorder",
        "channelconfiguration_set__recorder__model",
        "channelconfiguration_set__recorder__model__provider",
        "channelconfiguration_set__recording_format",
    )
    serializer_class = DeploymentSerializerWithChannel
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]


class ChannelConfigurationViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = ChannelConfiguration.objects.select_related(
        "deployment",
        "deployment__project",
        "deployment__project__project_type",
        "deployment__provider",
        "deployment__campaign",
        "deployment__campaign__project",
        "deployment__site",
        "deployment__site__project",
        "deployment__platform",
        "deployment__platform__type",
        "hydrophone",
        "hydrophone__model",
        "hydrophone__model__provider",
        "recorder",
        "recorder__model",
        "recorder__model__provider",
        "recording_format",
    ).prefetch_related(
        "deployment__project__responsible_parties",
    )
    serializer_class = ChannelConfigurationSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
