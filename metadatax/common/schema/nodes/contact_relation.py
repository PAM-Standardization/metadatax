import graphene
from django_extension.schema.types import ExtendedNode

from metadatax.common.models import Person, Team, Institution, ContactRelation
from .institution import InstitutionNode
from .person import PersonNode
from .team import TeamNode
from ..enums import RoleEnum


class ContactRelationNode(ExtendedNode):
    role = RoleEnum()

    class Meta:
        model = ContactRelation
        exclude = ("contact_id",)
        filter_fields = {
        }

    contact_type = graphene.NonNull(graphene.String)

    def resolve_content_type(self: ContactRelation, info):
        return self.contact_type.model

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
