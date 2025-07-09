from graphene import relay, ID
from graphene_django import DjangoObjectType

from metadatax.bibliography.models import BibliographyConference


class BibliographyConferenceNode(DjangoObjectType):
    id = ID(required=True)

    class Meta:
        model = BibliographyConference
        fields = "__all__"
        interfaces = (relay.Node,)
