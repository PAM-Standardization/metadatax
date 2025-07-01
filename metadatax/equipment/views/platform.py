from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.equipment.models import Platform
from metadatax.equipment.serializers import PlatformSerializer


class PlatformViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = Platform.objects.select_related(
        "owner",
        "provider",
        "type",
    )
    serializer_class = PlatformSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
