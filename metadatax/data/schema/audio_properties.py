from django_filters import FilterSet, NumberFilter
from graphene import ID, relay
from graphene_django import DjangoObjectType

from metadatax.data.models import AudioProperties


class AudioPropertiesFilter(FilterSet):
    file__id = NumberFilter()

    class Meta:
        model = AudioProperties
        fields = {
            "id": ["exact", "in"],
            "file__id": ["exact", "in"],
            "sampling_frequency": ["exact", "lt", "lte", "gt", "gte"],
            "initial_timestamp": ["exact", "lt", "lte", "gt", "gte"],
            "duration": ["exact", "lt", "lte", "gt", "gte"],
            "sample_depth": ["exact", "lt", "lte", "gt", "gte"],
        }


class AudioPropertiesNode(DjangoObjectType):
    id = ID(required=True)

    class Meta:
        model = AudioProperties
        fields = "__all__"
        filterset_class = AudioPropertiesFilter
        interfaces = (relay.Node,)
