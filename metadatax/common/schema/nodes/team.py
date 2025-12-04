from graphene import relay, ID

from metadatax.common.models import Team
from metadatax.utils.schema import MxObjectType


class TeamNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = Team
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
        }
        interfaces = (relay.Node,)
