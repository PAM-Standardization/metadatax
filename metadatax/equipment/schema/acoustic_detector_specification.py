from django_filters import FilterSet, NumberFilter
from graphene import ID, relay

from metadatax.equipment.models import AcousticDetectorSpecification
from metadatax.utils.schema import MxObjectType


class AcousticDetectorSpecificationFilter(FilterSet):
    detected_labels__id = NumberFilter()

    class Meta:
        model = AcousticDetectorSpecification
        fields = {
            "id": ["exact", "in"],
            "detected_labels__id": ["exact", "in"],
            "detected_labels__nickname": ["exact", "icontains"],
            "detected_labels__source__english_name": ["exact", "icontains"],
            "min_frequency": ["exact", "lt", "lte", "gt", "gte"],
            "max_frequency": ["exact", "lt", "lte", "gt", "gte"],
            "algorithm_name": ["exact", "icontains"],
        }


class AcousticDetectorSpecificationNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = AcousticDetectorSpecification
        fields = "__all__"
        filterset_class = AcousticDetectorSpecificationFilter
        interfaces = (relay.Node,)
