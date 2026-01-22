from django_extension.schema.types import ExtendedEnumType

from metadatax.acquisition.models import Financing

__all__ = [
    'FinancingEnum',
]

class FinancingEnum(ExtendedEnumType):

    class Meta:
        enum = Financing

    Public = 'PU'
    Private = 'PR'
    Mixte = 'MI'
    NotFinanced = 'NF'
