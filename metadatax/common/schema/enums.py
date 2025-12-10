import graphene

from metadatax.common.models import Role, Accessibility

__all__ = [
    'AccessibilityEnum',
    'RoleEnum',
]


class RoleEnum(graphene.Enum):
    class Meta:
        enum = Role


class AccessibilityEnum(graphene.Enum):
    class Meta:
        enum = Accessibility
