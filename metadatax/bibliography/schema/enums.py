import graphene
from metadatax.bibliography.models import BibliographyStatus, BibliographyType

__all__ = [
    'BibliographyStatusEnum',
    'BibliographyTypeEnum',
]


class BibliographyStatusEnum(graphene.Enum):
    class Meta:
        enum = BibliographyStatus


class BibliographyTypeEnum(graphene.Enum):
    class Meta:
        enum = BibliographyType
