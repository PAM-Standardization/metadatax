from graphene import relay, ID

from metadatax.bibliography.models import BibliographyPoster
from metadatax.utils.schema import MxObjectType


class BibliographyPosterNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = BibliographyPoster
        fields = "__all__"
        interfaces = (relay.Node,)
