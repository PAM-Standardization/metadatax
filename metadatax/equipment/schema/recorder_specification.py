from django_filters import FilterSet, NumberFilter
from graphene import ID, relay
from graphene_django import DjangoObjectType

from metadatax.equipment.models import RecorderSpecification


class RecorderSpecificationFilter(FilterSet):
    equipment__id = NumberFilter()

    class Meta:
        model = RecorderSpecification
        fields = {
            "id": ["exact", "in"],
            "equipment__id": ["exact", "in"],
            "channels_count": ["exact", "lt", "lte", "gt", "gte"],
            "storage_slots_count": ["exact", "lt", "lte", "gt", "gte"],
            "storage_maximum_capacity": ["exact", "lt", "lte", "gt", "gte"],
            "storage_type": ["exact", "icontains"],
        }


class RecorderSpecificationNode(DjangoObjectType):
    id = ID(required=True)

    class Meta:
        model = RecorderSpecification
        fields = "__all__"
        filterset_class = RecorderSpecificationFilter
        interfaces = (relay.Node,)
