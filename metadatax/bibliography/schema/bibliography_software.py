from graphene import relay, ID
from graphene_django import DjangoObjectType

from metadatax.bibliography.models import BibliographySoftware


class BibliographySoftwareNode(DjangoObjectType):
    id = ID(required=True)

    class Meta:
        model = BibliographySoftware
        fields = "__all__"
        interfaces = (relay.Node,)
