from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.models.data import File
from metadatax.serializers.data import FileSerializer


class FileViewSet(mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
