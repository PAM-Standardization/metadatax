from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.acquisition.models import Project
from metadatax.acquisition.serializers import ProjectSerializer


class ProjectViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = Project.objects.select_related("project_type",).prefetch_related(
        "contacts",
        "contacts__contact",
        "contacts__institution",
    )
    serializer_class = ProjectSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    search_fields = [
        "name",
        "contacts__role",
        "contacts__contact__first_name",
        "contacts__contact__last_name",
        "contacts__contact__mail",
        "contacts__institution__name",
        "contacts__institution__mail",
        "accessibility",
        "doi",
        "project_type__name",
        "project_goal",
        "financing",
    ]
