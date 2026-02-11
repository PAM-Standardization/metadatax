from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.common.admin import TeamAdmin
from metadatax.common.models import Team
from metadatax.common.serializers import TeamSerializer


class TeamViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = Team.objects.select_related("institution")
    serializer_class = TeamSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    search_fields = TeamAdmin.search_fields
