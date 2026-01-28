from django_filters import FilterSet
from graphene import ID, relay

from metadatax.equipment.models import RecorderSpecification
from metadatax.utils.schema import MxObjectType


class RecorderSpecificationFilter(FilterSet):
    class Meta:
        model = RecorderSpecification
        fields = {
            "id": ["exact", "in"],
            "channels_count": ["exact", "lt", "lte", "gt", "gte"],
            "storage_slots_count": ["exact", "lt", "lte", "gt", "gte"],
            # "storage_maximum_capacity": ["exact", "lt", "lte", "gt", "gte"], # TODO
            "storage_type": ["exact", "icontains"],
        }


class RecorderSpecificationNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = RecorderSpecification
        fields = "__all__"
        filterset_class = RecorderSpecificationFilter
        interfaces = (relay.Node,)
