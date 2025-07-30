from graphene import relay, ID

from metadatax.bibliography.models import BibliographyArticle
from metadatax.utils.schema import MxObjectType


class BibliographyArticleNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = BibliographyArticle
        fields = "__all__"
        interfaces = (relay.Node,)
