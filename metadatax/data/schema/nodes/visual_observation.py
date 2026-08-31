from django_extension.schema.types import ExtendedNode
from graphene import NonNull

from metadatax.common.schema import PersonNode
from metadatax.data.models import VisualObservation
from metadatax.ontology.schema import SourceNode


class VisualObservationNode(ExtendedNode):
    source = NonNull(SourceNode)
    observer = PersonNode()

    class Meta:
        model = VisualObservation
        fields = '__all__'
