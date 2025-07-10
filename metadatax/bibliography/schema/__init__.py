import graphene
from graphene import ObjectType, Field
from graphene_django_pagination import DjangoPaginationConnectionField

from metadatax.bibliography.models import (
    BibliographyArticle,
    BibliographySoftware,
    BibliographyPoster,
    BibliographyConference,
    Bibliography,
    Tag,
    Author,
)
from .author import AuthorNode
from .bibliography import BibliographyNode
from .bibliography_article import BibliographyArticleNode
from .bibliography_conference import BibliographyConferenceNode
from .bibliography_poster import BibliographyPosterNode
from .bibliography_software import BibliographySoftwareNode
from .tags import TagNode


class BibliographyQuery(ObjectType):

    all_authors = DjangoPaginationConnectionField(AuthorNode)
    author_by_id = Field(AuthorNode, id=graphene.ID(required=True))

    all_tags = DjangoPaginationConnectionField(TagNode)
    tag_by_id = Field(TagNode, id=graphene.ID(required=True))

    all_bibliography = DjangoPaginationConnectionField(BibliographyNode)
    bibliography_by_id = Field(BibliographyNode, id=graphene.ID(required=True))

    bibliography_article_by_id = Field(
        BibliographyArticleNode, id=graphene.ID(required=True)
    )
    bibliography_software_by_id = Field(
        BibliographySoftwareNode, id=graphene.ID(required=True)
    )
    bibliography_poster_by_id = Field(
        BibliographyPosterNode, id=graphene.ID(required=True)
    )
    bibliography_conference_by_id = Field(
        BibliographyConferenceNode, id=graphene.ID(required=True)
    )

    def resolve_author_by_id(self, info, id):
        return Author.objects.get(pk=id)

    def resolve_tag_by_id(self, info, id):
        return Tag.objects.get(pk=id)

    def resolve_bibliography_by_id(self, info, id):
        return Bibliography.objects.get(pk=id)

    def resolve_bibliography_article_by_id(self, info, id):
        return BibliographyArticle.objects.get(pk=id)

    def resolve_bibliography_software_by_id(self, info, id):
        return BibliographySoftware.objects.get(pk=id)

    def resolve_bibliography_poster_by_id(self, info, id):
        return BibliographyPoster.objects.get(pk=id)

    def resolve_bibliography_conference_by_id(self, info, id):
        return BibliographyConference.objects.get(pk=id)
