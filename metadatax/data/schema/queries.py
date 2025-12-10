import graphene
from graphene import ObjectType, relay
from graphene_django_pagination import DjangoPaginationConnectionField
from django_extended.schema.fields import ByIdField

from .nodes import *
from .unions import FileUnionConnection, FileUnion
from ..models import AudioFile, DetectionFile


class DataQuery(ObjectType):
    # File Format
    all_file_formats = DjangoPaginationConnectionField(FileFormatNode)
    file_format_by_id = ByIdField(FileFormatNode)

    # Audio File
    all_audio_files = DjangoPaginationConnectionField(AudioFileNode)
    audio_file_by_id = ByIdField(AudioFileNode)
    # Detection File
    all_detection_files = DjangoPaginationConnectionField(DetectionFileNode)
    detection_file_by_id = ByIdField(DetectionFileNode)

    # Files
    all_files = relay.ConnectionField(FileUnionConnection)
    file_by_id = graphene.Field(FileUnion, id=graphene.ID(required=True))

    def resolve_all_files(self, info, **kwargs):
        data = []
        if AudioFile.objects.exists():
            data += list(AudioFile.objects.all())
        if DetectionFile.objects.exists():
            data += list(DetectionFile.objects.all())
        return data

    def resolve_file_by_id(self, info, id: int, **kwargs):
        for qs in [AudioFile.objects.all(), DetectionFile.objects.all()]:
            if qs.filter(pk=id).exists():
                return qs.get(pk=id)
