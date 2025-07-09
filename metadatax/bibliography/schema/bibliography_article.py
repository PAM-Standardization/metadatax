from graphene import relay, ID
from graphene_django import DjangoObjectType

from metadatax.bibliography.models import BibliographyArticle


class BibliographyArticleNode(DjangoObjectType):
    id = ID(required=True)

    class Meta:
        model = BibliographyArticle
        fields = "__all__"
        interfaces = (relay.Node,)
