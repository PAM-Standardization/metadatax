from graphene import relay, ID

from metadatax.bibliography.models import BibliographyConference
from metadatax.utils.schema import MxObjectType


class BibliographyConferenceNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = BibliographyConference
        fields = "__all__"
        interfaces = (relay.Node,)
