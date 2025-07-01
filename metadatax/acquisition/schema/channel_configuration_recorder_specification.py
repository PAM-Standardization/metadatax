from django_filters import FilterSet, NumberFilter, CharFilter
from graphene import ID, relay
from graphene_django import DjangoObjectType

from metadatax.acquisition.models import ChannelConfigurationRecorderSpecification


class ChannelConfigurationRecorderSpecificationFilter(FilterSet):
    channel_configuration__id = NumberFilter()
    recording_formats = CharFilter(field_name="recording_formats__name")

    class Meta:
        model = ChannelConfigurationRecorderSpecification
        fields = {
            "id": ["exact", "in"],
            "hydrophone_id": ["exact", "in"],
            "recorder_id": ["exact", "in"],
            "channel_configuration__id": ["exact", "in"],
        }


class ChannelConfigurationRecorderSpecificationNode(DjangoObjectType):
    id = ID(required=True)

    class Meta:
        model = ChannelConfigurationRecorderSpecification
        fields = "__all__"
        filterset_class = ChannelConfigurationRecorderSpecificationFilter
        interfaces = (relay.Node,)
