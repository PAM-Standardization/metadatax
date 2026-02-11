from django_extension.schema.types import ExtendedNode

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
