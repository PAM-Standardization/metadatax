from graphene import relay, ID

from metadatax.bibliography.models import Tag
from metadatax.utils.schema import MxObjectType


class TagNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = Tag
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
        }
        interfaces = (relay.Node,)
