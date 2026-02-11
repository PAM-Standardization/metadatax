from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.data.admin import AudioFileAdmin
from metadatax.data.models import AudioFile
from metadatax.data.serializers import AudioFileSerializer


class AudioFileViewSet(mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet):
    queryset = AudioFile.objects.select_related("format")
    serializer_class = AudioFileSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    search_fields = AudioFileAdmin.search_fields
