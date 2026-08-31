from django_extension.schema.types import ExtendedNode

from metadatax.ontology.models import Behavior


class BehaviorNode(ExtendedNode):
    class Meta:
        model = Behavior
        fields = "__all__"
        filter_fields = {}
