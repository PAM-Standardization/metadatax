from django_extension.schema.types import ExtendedEnumType

from metadatax.common.models import Role, Accessibility

__all__ = [
    'AccessibilityEnum',
    'RoleEnum',
]


class RoleEnum(ExtendedEnumType):
    class Meta:
        enum = Role

    MainContact = 'MC'
    Funder = 'F'
    ProjectOwner = 'PO'
    ProjectManager = 'PM'
    DatasetSupplier = 'DS'
    DatasetProducer = 'DP'
    ProductionDatabase = 'PD'
    ContactPoint = 'CP'


class AccessibilityEnum(ExtendedEnumType):
    class Meta:
        enum = Accessibility

    Confidential = 'C'
    UponRequest = 'R'
    OpenAccess = 'O'
