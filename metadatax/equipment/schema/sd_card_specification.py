from django_filters import FilterSet, NumberFilter
from graphene import ID, relay
from graphene_django import DjangoObjectType

from metadatax.equipment.models import SDCardSpecification


class SDCardSpecificationFilter(FilterSet):
    equipment__id = NumberFilter()

    class Meta:
        model = SDCardSpecification
        fields = {
            "id": ["exact", "in"],
            "equipment__id": ["exact", "in"],
            "capacity": ["exact", "lt", "lte", "gt", "gte"],
        }


class SDCardSpecificationNode(DjangoObjectType):
    id = ID(required=True)

    class Meta:
        model = SDCardSpecification
        fields = "__all__"
        filterset_class = SDCardSpecificationFilter
        interfaces = (relay.Node,)
