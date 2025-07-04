from django_filters import FilterSet, NumberFilter
from graphene import ID, relay
from graphene_django import DjangoObjectType

from metadatax.acquisition.models import ProjectType


class ProjectTypeFilter(FilterSet):

    projects__id = NumberFilter()

    class Meta:
        model = ProjectType
        fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
            "projects__id": ["exact", "in"],
        }


class ProjectTypeNode(DjangoObjectType):
    id = ID(required=True)

    class Meta:
        model = ProjectType
        fields = "__all__"
        filterset_class = ProjectTypeFilter
        interfaces = (relay.Node,)
