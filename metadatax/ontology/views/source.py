from django_extension.filters import ModelFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.ontology.models import Source
from metadatax.ontology.serializers import SourceSerializer


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    filter_backends = [
        DjangoFilterBackend,
        ModelFilter,
    ]
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
