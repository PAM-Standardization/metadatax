from django_extension.schema.types import ExtendedNode

from metadatax.common.models import Tag


class TagNode(ExtendedNode):
    class Meta:
        model = Tag
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
        }
