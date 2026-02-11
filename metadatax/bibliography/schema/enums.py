import graphene
from django_extension.schema.types import ExtendedEnumType

from metadatax.bibliography.models import BibliographyStatus, BibliographyType

__all__ = [
    'BibliographyStatusEnum',
    'BibliographyTypeEnum',
]


class BibliographyStatusEnum(ExtendedEnumType):
    class Meta:
        enum = BibliographyStatus

    Upcoming = 'U'
    Published = 'P'


class BibliographyTypeEnum(ExtendedEnumType):
    class Meta:
        enum = BibliographyType

    Software = 'S'
    Article = 'A'
    Conference = 'C'
    Poster = 'P'
