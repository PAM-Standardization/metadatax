from django_extended.schema.interfaces import ExtendedInterface
from django_extended.schema.types import ExtendedNode

from metadatax.equipment.models import StorageSpecification


class StorageSpecificationNode(ExtendedNode):
    class Meta:
        model = StorageSpecification
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "type": ["exact", "icontains"],
            # "capacity": ["exact", "lt", "lte", "gt", "gte"], # TODO
        }
        interfaces = (ExtendedInterface,)
