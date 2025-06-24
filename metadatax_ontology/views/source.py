from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax_ontology.models import Source
from metadatax_ontology.serializers import SourceSerializer
from utils.views import ModelFilter


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
