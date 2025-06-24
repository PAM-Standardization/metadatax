from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax_acquisition.models import Site
from metadatax_acquisition.serializers import SiteSerializer


class SiteViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
