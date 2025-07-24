from django_filters import FilterSet, NumberFilter
from graphene import ID, relay
from graphene_django import DjangoObjectType

from metadatax.ontology.models import Label
from .physical_descriptor import SignalShapeEnum, SignalPluralityEnum


class LabelFilter(FilterSet):
    labels__id = NumberFilter()
    children__id = NumberFilter()
    acoustic_detectors__id = NumberFilter()
    channel_configuration_detector_specifications__id = NumberFilter()

    class Meta:
        model = Label
        fields = {
            "id": ["exact", "in"],
            "source_id": ["exact", "in"],
            "sound_id": ["exact", "in"],
            "parent_id": ["exact", "in"],
            "children__id": ["exact", "in"],
            "nickname": ["exact", "icontains"],
            # "associated_names": [
            #     "icontains",
            # ], # TODO
            "acoustic_detectors__id": ["exact", "in"],
            "channel_configuration_detector_specifications__id": ["exact", "in"],
            "shape": [
                "exact",
            ],
            "plurality": [
                "exact",
            ],
            "min_frequency": ["exact", "lt", "lte", "gt", "gte"],
            "max_frequency": ["exact", "lt", "lte", "gt", "gte"],
            "mean_duration": ["exact", "lt", "lte", "gt", "gte"],
        }


class LabelNode(DjangoObjectType):
    id = ID(required=True)
    shape = SignalShapeEnum()
    plurality = SignalPluralityEnum()

    class Meta:
        model = Label
        fields = "__all__"
        filterset_class = LabelFilter
        interfaces = (relay.Node,)
