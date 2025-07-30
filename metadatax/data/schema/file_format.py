from django_filters import FilterSet, NumberFilter
from graphene import ID, relay

from metadatax.data.models import FileFormat
from metadatax.utils.schema import MxObjectType


class FileFormatFilter(FilterSet):
    channel_configuration_recorder_specifications__id = NumberFilter()
    channel_configuration_detector_specifications__id = NumberFilter()
    files__id = NumberFilter()

    class Meta:
        model = FileFormat
        fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
            "channel_configuration_recorder_specifications__id": ["exact", "in"],
            "channel_configuration_detector_specifications__id": ["exact", "in"],
            "files__id": ["exact", "in"],
        }


class FileFormatNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = FileFormat
        fields = "__all__"
        filterset_class = FileFormatFilter
        interfaces = (relay.Node,)
