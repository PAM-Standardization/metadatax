from django_filters import FilterSet, CharFilter, NumberFilter
from graphene import ID, relay

from metadatax.common.schema import AccessibilityEnum
from metadatax.data.models import File
from metadatax.utils.schema import MxObjectType


class FileFilter(FilterSet):
    format = CharFilter(field_name="format__name")
    channel_configurations__id = NumberFilter()

    class Meta:
        model = File
        fields = {
            "id": ["exact", "in"],
            "filename": ["exact", "icontains"],
            "format": ["exact"],
            "audio_properties_id": ["exact", "in"],
            "detection_properties_id": ["exact", "in"],
            "storage_location": ["exact", "icontains"],
            "file_size": ["exact", "lt", "lte", "gt", "gte"],
            "accessibility": ["exact"],
            "channel_configurations__id": ["exact", "in"],
        }


class FileNode(MxObjectType):
    id = ID(required=True)
    accessibility = AccessibilityEnum()

    class Meta:
        model = File
        fields = "__all__"
        filterset_class = FileFilter
        interfaces = (relay.Node,)
