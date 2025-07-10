from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.equipment.models import Maintenance
from metadatax.equipment.serializers import MaintenanceSerializer


class MaintenanceViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = Maintenance.objects.select_related(
        "type",
        "maintainer",
        "maintainer_institution",
    )
    serializer_class = MaintenanceSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
