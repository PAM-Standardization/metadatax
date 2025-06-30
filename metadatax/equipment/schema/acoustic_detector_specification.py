from django_filters import FilterSet, NumberFilter
from graphene import ID, relay
from graphene_django import DjangoObjectType

from metadatax.equipment.models import AcousticDetectorSpecification


class AcousticDetectorSpecificationFilter(FilterSet):
    detected_labels__id = NumberFilter()
    equipment__id = NumberFilter()

    class Meta:
        model = AcousticDetectorSpecification
        fields = {
            "id": ["exact", "in"],
            "equipment__id": ["exact", "in"],
            "detected_labels__id": ["exact", "in"],
            "min_frequency": ["exact", "lt", "lte", "gt", "gte"],
            "max_frequency": ["exact", "lt", "lte", "gt", "gte"],
            "algorithm_name": ["exact", "icontains"],
        }


class AcousticDetectorSpecificationNode(DjangoObjectType):
    id = ID(required=True)

    class Meta:
        model = AcousticDetectorSpecification
        fields = "__all__"
        filterset_class = AcousticDetectorSpecificationFilter
        interfaces = (relay.Node,)
