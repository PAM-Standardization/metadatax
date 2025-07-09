from graphene import relay, ID
from graphene_django import DjangoObjectType

from metadatax.bibliography.models import BibliographyPoster


class BibliographyPosterNode(DjangoObjectType):
    id = ID(required=True)

    class Meta:
        model = BibliographyPoster
        fields = "__all__"
        interfaces = (relay.Node,)
