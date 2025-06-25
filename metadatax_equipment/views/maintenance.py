from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax_equipment.models import Maintenance
from metadatax_equipment.serializers import MaintenanceSerializer


class MaintenanceViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = Maintenance.objects.select_related(
        "type",
        "maintainer",
    )
    serializer_class = MaintenanceSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
