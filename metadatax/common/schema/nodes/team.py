from django_extension.schema.types import ExtendedNode

from metadatax.common.models import Team


class TeamNode(ExtendedNode):
    class Meta:
        model = Team
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
        }
