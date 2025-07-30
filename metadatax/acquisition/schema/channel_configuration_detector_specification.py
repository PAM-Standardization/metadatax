from django_filters import FilterSet, NumberFilter, CharFilter
from graphene import ID, relay

from metadatax.acquisition.models import ChannelConfigurationDetectorSpecification
from metadatax.utils.schema import MxObjectType


class ChannelConfigurationDetectorSpecificationFilter(FilterSet):
    channel_configuration__id = NumberFilter()
    labels__id = NumberFilter()
    output_formats = CharFilter(field_name="output_formats__name")

    class Meta:
        model = ChannelConfigurationDetectorSpecification
        fields = {
            "id": ["exact", "in"],
            "detector_id": ["exact", "in"],
            "labels__id": ["exact", "in"],
            "channel_configuration__id": ["exact", "in"],
        }


class ChannelConfigurationDetectorSpecificationNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = ChannelConfigurationDetectorSpecification
        fields = "__all__"
        filterset_class = ChannelConfigurationDetectorSpecificationFilter
        interfaces = (relay.Node,)
