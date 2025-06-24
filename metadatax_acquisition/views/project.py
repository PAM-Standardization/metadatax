from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax_acquisition.models import Project
from metadatax_acquisition.serializers import ProjectSerializer


class ProjectViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = Project.objects.select_related("project_type", ).prefetch_related(
        "contacts",
        "contacts__contact",
    )
    serializer_class = ProjectSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
