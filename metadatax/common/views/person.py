from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.common.admin import PersonAdmin
from metadatax.common.models import Person
from metadatax.common.serializers import PersonSerializer


class PersonViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = Person.objects.prefetch_related(
        "institutions",
        "teams",
        "teams__institution",
    )
    serializer_class = PersonSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    search_fields = PersonAdmin.search_fields
