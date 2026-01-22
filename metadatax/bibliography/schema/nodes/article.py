import graphene
from django_extension.schema.types import ExtendedNode

from metadatax.bibliography.models import Article
from metadatax.bibliography.schema import BibliographyTypeEnum
from metadatax.bibliography.schema.enums import BibliographyStatusEnum
from metadatax.common.schema.nodes.tag import TagNode


class ArticleNode(ExtendedNode):
    type = graphene.NonNull(BibliographyTypeEnum)
    status = graphene.NonNull(BibliographyStatusEnum)

    tags = graphene.List(TagNode)

    journal = graphene.String(required=True)

    class Meta:
        model = Article
        exclude = (
            "conference_name",
            "conference_location",
            "conference_abstract_book_url",
            "poster_url",
            "publication_place",
            "repository_url",
        )
        filter_fields = {
            "id": ["exact", "in"],
            "type": ["exact", "in"],
            "title": ["exact", "icontains"],
            "journal": ["exact", "icontains"],
            "doi": ["exact"],
            "status": ["exact"],
            "publication_date": ["exact", "lt", "lte", "gt", "gte"],
        }
