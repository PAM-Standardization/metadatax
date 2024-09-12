"""Acquisition models for metadata app"""
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.models.equipment import Hydrophone, Recorder
from metadatax.serializers.equipment import (
    HydrophoneSerializer,
    RecorderSerializer,
)


class HydrophoneViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = Hydrophone.objects.select_related("model", "model__provider")
    serializer_class = HydrophoneSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]


class RecorderViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = Recorder.objects.select_related("model", "model__provider")
    serializer_class = RecorderSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
