from django_extended.schema.interfaces import ExtendedInterface
from django_extended.schema.types import ExtendedNode
import graphene

from metadatax.bibliography.models import Conference
from metadatax.bibliography.schema.enums import BibliographyStatusEnum, BibliographyTypeEnum
from metadatax.common.schema.nodes.tag import TagNode


class ConferenceNode(ExtendedNode):
    type = graphene.NonNull(BibliographyTypeEnum)
    status = graphene.NonNull(BibliographyStatusEnum)

    tags = graphene.List(TagNode)

    conference_name = graphene.String(required=True)
    conference_location = graphene.String(required=True)

    class Meta:
        model = Conference
        exclude = (
            "journal",
            "volumes",
            "pages_from",
            "pages_to",
            "issue_nb",
            "article_nb",
            "publication_place",
            "repository_url",
            "poster_url",
        )
        filter_fields = {
            "id": ["exact", "in"],
            "type": ["exact", "in"],
            "title": ["exact", "icontains"],
            "conference_name": ["exact", "icontains"],
            "conference_location": ["exact", "icontains"],
            "doi": ["exact"],
            "status": ["exact"],
            "publication_date": ["exact", "lt", "lte", "gt", "gte"],
        }
        interfaces = (ExtendedInterface,)
