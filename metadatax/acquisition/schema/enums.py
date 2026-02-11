from django_extension.schema.types import ExtendedEnumType

from metadatax.acquisition.models import Financing, ChannelConfigurationStatus

__all__ = [
    'FinancingEnum',
    'ChannelConfigurationStatusEnum',
]


class FinancingEnum(ExtendedEnumType):
    class Meta:
        enum = Financing

    Public = 'PU'
    Private = 'PR'
    Mixte = 'MI'
    NotFinanced = 'NF'


class ChannelConfigurationStatusEnum(ExtendedEnumType):
    class Meta:
        enum = ChannelConfigurationStatus

    Active = "A"
    Failed = "F"
    Lost = "L"
