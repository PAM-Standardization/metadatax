from django_extended.viewsets import ModelFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.ontology.models import Label
from metadatax.ontology.serializers import LabelSerializer


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    filter_backends = [
        DjangoFilterBackend,
        ModelFilter,
    ]
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
