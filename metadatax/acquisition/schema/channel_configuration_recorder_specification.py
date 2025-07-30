from django_filters import FilterSet, NumberFilter, CharFilter
from graphene import ID, relay

from metadatax.acquisition.models import ChannelConfigurationRecorderSpecification
from metadatax.utils.schema import MxObjectType


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


class ChannelConfigurationRecorderSpecificationNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = ChannelConfigurationRecorderSpecification
        fields = "__all__"
        filterset_class = ChannelConfigurationRecorderSpecificationFilter
        interfaces = (relay.Node,)
