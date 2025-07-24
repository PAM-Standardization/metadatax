from django_filters import FilterSet, CharFilter, BooleanFilter, NumberFilter
from graphene import ID, relay
from graphene_django import DjangoObjectType

from metadatax.equipment.models import Platform


class PlatformFilter(FilterSet):
    type = CharFilter(field_name="type__name")
    is_mobile = BooleanFilter(field_name="type__is_mobile")
    deployments__id = NumberFilter()
    maintenances__id = NumberFilter()

    class Meta:
        model = Platform
        fields = {
            "id": ["exact", "in"],
            "owner_id": ["exact", "in"],
            "provider_id": ["exact", "in"],
            "deployments__id": ["exact", "in"],
            "maintenances__id": ["exact", "in"],
            "name": ["exact", "icontains"],
        }


class PlatformNode(DjangoObjectType):
    id = ID(required=True)

    class Meta:
        model = Platform
        fields = "__all__"
        filterset_class = PlatformFilter
        interfaces = (relay.Node,)
