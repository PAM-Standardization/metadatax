from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.common.models import Institution
from metadatax.common.serializers.institution import InstitutionSerializer


class InstitutionViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    search_fields = ("name", "city", "country", "mail", "website")
