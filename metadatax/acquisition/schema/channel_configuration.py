from django_filters import FilterSet, NumberFilter
from graphene import ID, relay
from graphene_django import DjangoObjectType

from metadatax.acquisition.models import ChannelConfiguration


class ChannelConfigurationFilter(FilterSet):

    files__id = NumberFilter()
    storages__id = NumberFilter()

    class Meta:
        model = ChannelConfiguration
        fields = {
            "id": ["exact", "in"],
            "recorder_specification": ["isnull"],
            "detector_specification": ["isnull"],
            "deployment_id": ["exact", "in"],
            "continuous": ["exact"],
            "duty_cycle_on": ["exact", "lt", "lte", "gt", "gte"],
            "duty_cycle_off": ["exact", "lt", "lte", "gt", "gte"],
            "instrument_depth": ["exact", "lt", "lte", "gt", "gte"],
            "timezone": ["exact"],
            "harvest_starting_date": ["exact", "lt", "lte", "gt", "gte"],
            "harvest_ending_date": ["exact", "lt", "lte", "gt", "gte"],
            "files__id": ["exact", "in"],
            "storages__id": ["exact", "in"],
        }


class ChannelConfigurationNode(DjangoObjectType):
    id = ID(required=True)

    class Meta:
        model = ChannelConfiguration
        fields = "__all__"
        filterset_class = ChannelConfigurationFilter
        interfaces = (relay.Node,)
