from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.data.admin import DetectionFileAdmin
from metadatax.data.models import DetectionFile
from metadatax.data.serializers import DetectionFileSerializer


class DetectionFileViewSet(mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet):
    queryset = DetectionFile.objects.select_related("format")
    serializer_class = DetectionFileSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    search_fields = DetectionFileAdmin.search_fields
