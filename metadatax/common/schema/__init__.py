from graphene import ObjectType, Field, Int
from graphene_django_pagination import DjangoPaginationConnectionField

from metadatax.common.models import Contact, ContactRole
from .accessibility import AccessibilityEnum
from .contact import ContactNode
from .contact_role import ContactRoleNode, RoleEnum


class CommonQuery(ObjectType):
    all_contacts = DjangoPaginationConnectionField(ContactNode)
    contact_by_id = Field(ContactNode, id=Int())

    all_contact_roles = DjangoPaginationConnectionField(ContactRoleNode)
    contact_role_by_id = Field(ContactRoleNode, id=Int())

    def resolve_contact_by_id(self, info, id: int):
        return Contact.objects.get(pk=id)

    def resolve_contact_role_by_id(self, info, id: int):
        return ContactRole.objects.get(pk=id)
