import graphene
from graphene import ObjectType, Field
from graphene_django_pagination import DjangoPaginationConnectionField

from metadatax.common.models import Contact, ContactRole, Institution
from .accessibility import AccessibilityEnum
from .contact import ContactNode
from .contact_role import ContactRoleNode, RoleEnum
from .institution import InstitutionNode


class CommonQuery(ObjectType):
    all_contacts = DjangoPaginationConnectionField(ContactNode)
    contact_by_id = Field(ContactNode, id=graphene.ID(required=True))

    all_contact_roles = DjangoPaginationConnectionField(ContactRoleNode)
    contact_role_by_id = Field(ContactRoleNode, id=graphene.ID(required=True))

    all_institutions = DjangoPaginationConnectionField(InstitutionNode)
    institution_by_id = Field(InstitutionNode, id=graphene.ID(required=True))

    def resolve_contact_by_id(self, info, id: int):
        return Contact.objects.get(pk=id)

    def resolve_contact_role_by_id(self, info, id: int):
        return ContactRole.objects.get(pk=id)

    def resolve_institution_by_id(self, info, id: int):
        return Institution.objects.get(pk=id)
