from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.common.models import ContactRole
from metadatax.common.serializers import ContactRoleSerializer


class ContactRoleViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = ContactRole.objects.all().select_related("contact")
    serializer_class = ContactRoleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    search_fields = ("role", "contact__name", "contact__mail", "contact__website")
