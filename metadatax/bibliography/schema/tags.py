from graphene import relay, ID
from graphene_django import DjangoObjectType

from metadatax.bibliography.models import Tag


class TagNode(DjangoObjectType):
    id = ID(required=True)

    class Meta:
        model = Tag
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
        }
        interfaces = (relay.Node,)
