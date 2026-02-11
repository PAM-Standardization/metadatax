from django_extension.schema.types import ExtendedNode

from metadatax.ontology.models import Label
from metadatax.ontology.schema.enums import SignalShapeEnum, SignalPluralityEnum


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
            "parent_id": ["exact", "in"],
            "nickname": ["exact", "icontains"],
            # "associated_names": [
            #     "icontains",
            # ], # TODO
            "shape": ["exact"],
            "plurality": ["exact"],
            "min_frequency": ["exact", "lt", "lte", "gt", "gte"],
            "max_frequency": ["exact", "lt", "lte", "gt", "gte"],
            "mean_duration": ["exact", "lt", "lte", "gt", "gte"],
        }
