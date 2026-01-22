import graphene
from graphene import ObjectType, relay
from graphene_django_pagination import DjangoPaginationConnectionField
from django_extension.schema.fields import ByIdField

from metadatax.bibliography.models import Article, Software, Conference, Poster
from .unions import BibliographyUnionConnection, BibliographyUnion
from .nodes import *


class BibliographyQuery(ObjectType):
    # Author
    all_authors = DjangoPaginationConnectionField(AuthorNode)
    author_by_id = ByIdField(AuthorNode)

    # Article
    all_article = DjangoPaginationConnectionField(ArticleNode)
    article_by_id = ByIdField(ArticleNode)
    # Software
    all_software = DjangoPaginationConnectionField(SoftwareNode)
    software_by_id = ByIdField(SoftwareNode)
    # Conference
    all_conference = DjangoPaginationConnectionField(ConferenceNode)
    conference_by_id = ByIdField(ConferenceNode)
    # Poster
    all_poster = DjangoPaginationConnectionField(PosterNode)
    poster_by_id = ByIdField(PosterNode)

    # Bibliography
    all_bibliography = relay.ConnectionField(BibliographyUnionConnection)
    bibliography_by_id = graphene.Field(BibliographyUnion, id=graphene.ID(required=True))

    def resolve_all_bibliography(self, info, **kwargs):
        data = []
        if Article.objects.exists():
            data += list(Article.objects.all())
        if Software.objects.exists():
            data += list(Software.objects.all())
        if Conference.objects.exists():
            data += list(Conference.objects.all())
        if Poster.objects.exists():
            data += list(Poster.objects.all())
        return data

    def resolve_bibliography_by_id(self, info, id: int, **kwargs):
        for qs in [Article.objects.all(), Software.objects.all(), Conference.objects.all(), Poster.objects.all()]:
            if qs.filter(pk=id).exists():
                return qs.get(pk=id)
