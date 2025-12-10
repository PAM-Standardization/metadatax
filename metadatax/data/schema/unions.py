import graphene
from graphene import relay

from metadatax.data.models import File, AudioFile, DetectionFile
from .nodes import AudioFileNode, DetectionFileNode

__all__ = [
    'FileUnion',
    'FileUnionConnection'
]


class FileUnion(graphene.types.Union):
    class Meta:
        types = [
            AudioFileNode,
            DetectionFileNode,
        ]
        filter_fields = {
            "id": ["exact", "in"],
            "filename": ["exact", "icontains"],
            "storage_location": ["exact", "icontains"],
            "file_size": ["exact", "lt", "lte", "gt", "gte"],
            "accessibility": ["exact"],
        }

    @classmethod
    def resolve_type(cls, instance: File, info):
        if isinstance(instance, AudioFile):
            return AudioFileNode
        if isinstance(instance, DetectionFile):
            return DetectionFileNode
        return super().resolve_type(instance, info)


class FileUnionConnection(relay.Connection):
    class Meta:
        node = FileUnion
