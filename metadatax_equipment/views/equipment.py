from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax_equipment.models import Equipment
from metadatax_equipment.serializers import EquipmentSerializer


class EquipmentViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = Equipment.objects.select_related(
        "owner",
        "provider",
        "sd_card_specification",
        "recorder_specification",
        "hydrophone_specification",
        "acoustic_detector_specification",
    )
    serializer_class = EquipmentSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
