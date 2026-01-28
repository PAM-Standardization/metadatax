import graphene
from django_extension.schema.types import ExtendedNode
from metadatax.common.models import Person, Team, Institution, ContactRelation
from metadatax.common.schema.unions import ContactUnion

from .institution import InstitutionNode
from .person import PersonNode
from .team import TeamNode
from ..enums import RoleEnum


class ContactRelationNode(ExtendedNode):
    role = RoleEnum()

    class Meta:
        model = ContactRelation
        fields = (
            'role',
            'contact_type',
            'contact'
        )
        filter_fields = {
        }

    contact_type = graphene.NonNull(graphene.String)
    contact = ContactUnion()

    def resolve_contact_type(self: ContactRelation, info):
        return self.contact_type.model

    def resolve_contact(self: ContactRelation, info):
        return self.contact

    person = PersonNode()

    def resolve_person(self: ContactRelation, info):
        if self.contact_type.model == Person._meta.model_name:
            return Person.objects.get(pk=self.contact_id)

    team = TeamNode()

    def resolve_team(self: ContactRelation, info):
        if self.contact_type.model == Team._meta.model_name:
            return Team.objects.get(pk=self.contact_id)

    institution = InstitutionNode()

    def resolve_institution(self: ContactRelation, info):
        if self.contact_type.model == Institution._meta.model_name:
            return Institution.objects.get(pk=self.contact_id)
