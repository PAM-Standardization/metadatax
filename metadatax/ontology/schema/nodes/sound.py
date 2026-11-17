from django_extension.schema.types import ExtendedNode
import graphene
import graphene_django_optimizer

from metadatax.ontology.models import Sound, LabelDisplay
from ..enums import LabelDisplayEnum


class SoundNode(ExtendedNode):
    class Meta:
        model = Sound
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "parent_id": ["exact", "in"],
            "english_name": ["exact", "icontains"],
            "french_name": ["exact", "icontains"],
            "code_name": ["exact", "icontains"],
            "taxon": ["exact", "icontains"],
        }

    display = graphene.String(
        required=True,
        display=graphene.NonNull(LabelDisplayEnum)
    )

    @graphene_django_optimizer.resolver_hints()
    def resolve_display(self: Sound, info, display: LabelDisplay) -> str:
        return self.display(display.value)
