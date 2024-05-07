"""Acquisition models for metadata app"""
from rest_framework import viewsets, mixins
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.models.acquisition import (
    ChannelConfiguration,
    Deployment,
    Project,
    Institution
)
from metadatax.serializers.acquisition import (
    InstitutionSerializer,
    ProjectSerializer,
    DeploymentSerializer,
    ChannelConfigurationSerializer, )


class InstitutionViewSet(mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                         viewsets.ReadOnlyModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly,]
    filter_fields = [
        "name",
    ]


class ProjectViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly,]
    filter_fields = [
        "name",
    ]


class DeploymentViewSet(mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.ReadOnlyModelViewSet):
    queryset = Deployment.objects.all()
    serializer_class = DeploymentSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly,]
    filter_fields = [
        "name",
    ]


class ChannelConfigurationViewSet(mixins.CreateModelMixin,
                                  mixins.UpdateModelMixin,
                                  viewsets.ReadOnlyModelViewSet):
    queryset = ChannelConfiguration.objects.all()
    serializer_class = ChannelConfigurationSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly,]
    filter_fields = [
        "channel_name",
    ]
