from django_filters import FilterSet, NumberFilter
from graphene import ID, relay

from metadatax.equipment.models import StorageSpecification
from metadatax.utils.schema import MxObjectType


class StorageSpecificationFilter(FilterSet):
    equipment__id = NumberFilter()

    class Meta:
        model = StorageSpecification
        fields = {
            "id": ["exact", "in"],
            "equipment__id": ["exact", "in"],
            # "capacity": ["exact", "lt", "lte", "gt", "gte"], # TODO
        }


class StorageSpecificationNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = StorageSpecification
        fields = "__all__"
        filterset_class = StorageSpecificationFilter
        interfaces = (relay.Node,)
