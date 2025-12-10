import graphene
from graphene import relay
from metadatax.bibliography.models import Bibliography, Article, Poster, Software, Conference
from metadatax.bibliography.schema import ArticleNode, SoftwareNode, ConferenceNode, PosterNode

__all__ = [
    'BibliographyUnion',
    'BibliographyUnionConnection'
]


class BibliographyUnion(graphene.types.Union):
    class Meta:
        types = [
            ArticleNode,
            SoftwareNode,
            ConferenceNode,
            PosterNode,
        ]
        filter_fields = {
            "id": ["exact", "in"],
            "type": ["exact", "in"],
            "title": ["exact", "icontains"],
            "doi": ["exact"],
            "status": ["exact"],
            "publication_date": ["exact", "lt", "lte", "gt", "gte"],
        }

    @classmethod
    def resolve_type(cls, instance: Bibliography, info):
        if isinstance(instance, Article):
            return ArticleNode
        if isinstance(instance, Poster):
            return PosterNode
        if isinstance(instance, Software):
            return SoftwareNode
        if isinstance(instance, Conference):
            return ConferenceNode
        return super().resolve_type(instance, info)


class BibliographyUnionConnection(relay.Connection):
    class Meta:
        node = BibliographyUnion

    pass
