from django_extension.schema.types import ExtendedEnumType
import graphene

from metadatax.common.models import Role, Accessibility

__all__ = [
    'AccessibilityEnum',
    'RoleEnum',
    'ContactTypeEnum',
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


class ContactTypeEnum(graphene.Enum):
    person = 'person'
    team = 'team'
    institution = 'institution'

    @staticmethod
    def choices() -> list[tuple[str, str]]:
        return [
            (ContactTypeEnum.person, 'person'),
            (ContactTypeEnum.team, 'team'),
            (ContactTypeEnum.institution, 'institution'),
        ]
