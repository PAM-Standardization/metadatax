import graphene
from django_extension.schema.types import ExtendedNode

from metadatax.bibliography.models import Software
from metadatax.bibliography.schema.enums import BibliographyStatusEnum, BibliographyTypeEnum
from metadatax.common.schema.nodes.tag import TagNode


class SoftwareNode(ExtendedNode):
    type = graphene.NonNull(BibliographyTypeEnum)
    status = graphene.NonNull(BibliographyStatusEnum)

    tags = graphene.List(TagNode)

    publication_place = graphene.String(required=True)

    class Meta:
        model = Software
        exclude = (
            "journal",
            "volumes",
            "pages_from",
            "pages_to",
            "issue_nb",
            "article_nb",
            "conference_name",
            "conference_location",
            "conference_abstract_book_url",
            "poster_url",
        )
        filter_fields = {
            "id": ["exact", "in"],
            "type": ["exact", "in"],
            "title": ["exact", "icontains"],
            "publication_place": ["exact", "icontains"],
            "doi": ["exact"],
            "status": ["exact"],
            "publication_date": ["exact", "lt", "lte", "gt", "gte"],
        }
