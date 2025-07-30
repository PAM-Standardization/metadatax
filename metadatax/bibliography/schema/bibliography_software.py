from graphene import relay, ID

from metadatax.bibliography.models import BibliographySoftware
from metadatax.utils.schema import MxObjectType


class BibliographySoftwareNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = BibliographySoftware
        fields = "__all__"
        interfaces = (relay.Node,)
