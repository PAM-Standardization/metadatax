from django_filters import FilterSet, NumberFilter
from graphene import ID, relay
from graphene_django import DjangoObjectType

from metadatax.ontology.models import Label


class LabelFilter(FilterSet):
    physical_descriptor__id = NumberFilter()
    acoustic_detectors__id = NumberFilter()
    channel_configuration_detector_specifications__id = NumberFilter()

    class Meta:
        model = Label
        fields = {
            "id": ["exact", "in"],
            "source_id": ["exact", "in"],
            "sound_id": ["exact", "in"],
            "physical_descriptor__id": ["exact", "in"],
            "nickname": ["exact", "icontains"],
            "acoustic_detectors__id": ["exact", "in"],
            "channel_configuration_detector_specifications__id": ["exact", "in"],
        }


class LabelNode(DjangoObjectType):
    id = ID(required=True)

    class Meta:
        model = Label
        fields = "__all__"
        filterset_class = LabelFilter
        interfaces = (relay.Node,)
