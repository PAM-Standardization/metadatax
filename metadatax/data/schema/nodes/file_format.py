from django_extension.schema.types import ExtendedNode

from metadatax.data.models import FileFormat


class FileFormatNode(ExtendedNode):
    class Meta:
        model = FileFormat
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
        }
