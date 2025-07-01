from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.acquisition.models import Site
from metadatax.acquisition.serializers import SiteSerializer


class SiteViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    search_fields = ["name", "project__name"]
