from django_extended.schema.interfaces import ExtendedInterface
from django_extended.schema.types import ExtendedNode

from metadatax.bibliography.models import Author


class AuthorNode(ExtendedNode):
    class Meta:
        model = Author
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "order": ["exact", "lt", "lte", "gt", "gte"],
            "bibliography_id": ["exact", "in"],
            "person_id": ["exact", "in"],
        }
        interfaces = (ExtendedInterface,)
