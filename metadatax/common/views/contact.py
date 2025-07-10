from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.common.models import Contact
from metadatax.common.serializers import ContactSerializer


class ContactViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    search_fields = ("first_name", "last_name", "mail", "website")
