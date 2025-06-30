from django_filters import NumberFilter, FilterSet
from graphene import ID, relay
from graphene_django import DjangoObjectType

from metadatax.acquisition.models import Site


class SiteFilter(FilterSet):
    deployments__id = NumberFilter()

    class Meta:
        model = Site
        fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
            "project_id": ["exact", "in"],
            "deployments__id": ["exact", "in"],
        }


class SiteNode(DjangoObjectType):
    id = ID(required=True)

    class Meta:
        model = Site
        fields = "__all__"
        filterset_class = SiteFilter
        interfaces = (relay.Node,)
