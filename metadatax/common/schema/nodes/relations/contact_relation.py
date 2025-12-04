import graphene
from graphene import relay

from metadatax.common.models import Person, Team, Institution
from metadatax.common.models.relations import ContactRelation
from metadatax.common.schema import PersonNode, TeamNode, InstitutionNode
from metadatax.common.schema.enums import RoleEnum
from metadatax.utils.schema import MxObjectType


class ContactRelationNode(MxObjectType):

    role = graphene.NonNull(RoleEnum())
    contact_type = graphene.NonNull(graphene.String())

    person = PersonNode()
    team = TeamNode()
    institution = InstitutionNode()

    class Meta:
        model = ContactRelation
        exclude = ("contact_id",)
        filter_fields = {
        }
        interfaces = (relay.Node,)

    def resolve_content_type(self: ContactRelation, info):
        return self.contact_type.model

    def resolve_person(self: ContactRelation, info):
        if self.contact_type.model == Person._meta.model_name:
            return Person.objects.get(pk=self.contact_id)

    def resolve_team(self: ContactRelation, info):
        if self.contact_type.model == Team._meta.model_name:
            return Team.objects.get(pk=self.contact_id)

    def resolve_institution(self: ContactRelation, info):
        if self.contact_type.model == Institution._meta.model_name:
            return Institution.objects.get(pk=self.contact_id)
