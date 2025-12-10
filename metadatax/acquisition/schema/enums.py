import graphene
from metadatax.acquisition.models import Financing

__all__ = [
    'FinancingEnum',
]

class FinancingEnum(graphene.Enum):

    class Meta:
        enum = Financing

