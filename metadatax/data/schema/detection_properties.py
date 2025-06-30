from django_filters import FilterSet, NumberFilter
from graphene import ID, relay
from graphene_django import DjangoObjectType

from metadatax.data.models import DetectionProperties


class DetectionPropertiesFilter(FilterSet):
    file__id = NumberFilter()

    class Meta:
        model = DetectionProperties
        fields = {
            "id": ["exact", "in"],
            "file__id": ["exact", "in"],
            "start": ["exact", "lt", "lte", "gt", "gte"],
            "end": ["exact", "lt", "lte", "gt", "gte"],
        }


class DetectionPropertiesNode(DjangoObjectType):
    id = ID(required=True)

    class Meta:
        model = DetectionProperties
        fields = "__all__"
        filterset_class = DetectionPropertiesFilter
        interfaces = (relay.Node,)
