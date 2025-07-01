from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.ontology.models import PhysicalDescriptor
from metadatax.ontology.serializers import PhysicalDescriptorSerializer
from metadatax.utils import ModelFilter


class PhysicalDescriptorViewSet(viewsets.ModelViewSet):
    queryset = PhysicalDescriptor.objects.all()
    serializer_class = PhysicalDescriptorSerializer
    filter_backends = [
        DjangoFilterBackend,
        ModelFilter,
    ]
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
