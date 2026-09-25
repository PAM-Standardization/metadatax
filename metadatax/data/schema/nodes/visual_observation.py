from django_extension.schema.types import ExtendedNode
import graphene

from metadatax.common.schema import PersonNode
from metadatax.data.models import VisualObservation
from metadatax.ontology.schema import SourceNode, BehaviorNode


class VisualObservationNode(ExtendedNode):
    source = graphene.NonNull(SourceNode)
    observer = PersonNode()

    behaviors = graphene.List(BehaviorNode)
    reactions_to_boat = graphene.List(BehaviorNode)

    class Meta:
        model = VisualObservation
        fields = '__all__'
        filter_fields = {
        }
