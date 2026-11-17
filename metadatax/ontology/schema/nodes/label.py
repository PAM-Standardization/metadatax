from django_extension.schema.types import ExtendedNode
import graphene
import graphene_django_optimizer

from metadatax.ontology.models import Label, LabelDisplay
from ..enums import SignalShapeEnum, SignalPluralityEnum, LabelDisplayEnum


class LabelNode(ExtendedNode):
    shape = SignalShapeEnum()
    plurality = SignalPluralityEnum()

    class Meta:
        model = Label
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "source_id": ["exact", "in"],
            "sound_id": ["exact", "in"],
            "shape": ["exact"],
            "plurality": ["exact"],
            "min_frequency": ["exact", "lt", "lte", "gt", "gte"],
            "max_frequency": ["exact", "lt", "lte", "gt", "gte"],
            "mean_duration": ["exact", "lt", "lte", "gt", "gte"],
        }

    display = graphene.String(
        required=True,
        display=graphene.NonNull(LabelDisplayEnum)
    )

    @graphene_django_optimizer.resolver_hints()
    def resolve_display(self: Label, info, display: LabelDisplay) -> str:
        return self.display(display.value)
