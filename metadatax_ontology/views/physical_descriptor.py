from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax_ontology.models import PhysicalDescriptor
from metadatax_ontology.serializers import PhysicalDescriptorSerializer
from utils.views import ModelFilter


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
