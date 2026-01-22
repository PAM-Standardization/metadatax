import graphene
from django_extension.schema.types import ExtendedNode

from metadatax.equipment.models import AcousticDetectorSpecification
from metadatax.ontology.schema import LabelNode


class AcousticDetectorSpecificationNode(ExtendedNode):
    detected_labels = graphene.List(LabelNode)

    class Meta:
        model = AcousticDetectorSpecification
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "min_frequency": ["exact", "lt", "lte", "gt", "gte"],
            "max_frequency": ["exact", "lt", "lte", "gt", "gte"],
            "algorithm_name": ["exact", "icontains"],
        }
