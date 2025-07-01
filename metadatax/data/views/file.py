from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.data.models import File
from metadatax.data.serializers import FileSerializer


class FileViewSet(mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet):
    queryset = File.objects.select_related(
        "format",
        "audio_properties",
        "detection_properties",
    )
    serializer_class = FileSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
