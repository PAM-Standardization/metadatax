from graphene import ObjectType, Field
from graphene_django.filter import DjangoFilterConnectionField

from metadatax.data.models import AudioProperties, DetectionProperties, File, FileFormat
from .audio_properties import AudioPropertiesNode
from .detection_properties import DetectionPropertiesNode
from .file import FileNode
from .file_format import FileFormatNode


class DataQuery(ObjectType):

    all_audio_properties = DjangoFilterConnectionField(AudioPropertiesNode)
    audio_property_by_id = Field(AudioPropertiesNode)

    all_detection_properties = DjangoFilterConnectionField(DetectionPropertiesNode)
    detection_property_by_id = Field(DetectionPropertiesNode)

    all_file = DjangoFilterConnectionField(FileNode)
    file_by_id = Field(FileNode)

    all_file_formats = DjangoFilterConnectionField(FileFormatNode)
    file_format_by_id = Field(FileFormatNode)

    def resolve_audio_property_by_id(self, info, id):
        return AudioProperties.objects.get(pk=id)

    def resolve_detection_property_by_id(self, info, id):
        return DetectionProperties.objects.get(pk=id)

    def resolve_file_by_id(self, info, id: int):
        return File.objects.get(pk=id)

    def resolve_file_format_by_id(self, info, id: int):
        return FileFormat.objects.get(pk=id)
