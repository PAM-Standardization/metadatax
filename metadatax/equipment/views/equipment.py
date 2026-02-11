from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.equipment.models import Equipment
from metadatax.equipment.serializers import EquipmentSerializer


class EquipmentViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = Equipment.objects.select_related(
        "model",
    )
    serializer_class = EquipmentSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
