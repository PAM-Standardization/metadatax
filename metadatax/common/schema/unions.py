import graphene.types
from graphene import relay

from metadatax.common.models import Person, Team, Institution
from metadatax.common.schema.nodes.institution import InstitutionNode
from metadatax.common.schema.nodes.team import TeamNode
from metadatax.common.schema.nodes.person import PersonNode


class ContactUnion(graphene.types.Union):
    class Meta:
        types = [
            PersonNode,
            TeamNode,
            InstitutionNode,
        ]

    @classmethod
    def resolve_type(cls, instance: any, info):
        if isinstance(instance, Person):
            return PersonNode
        if isinstance(instance, Team):
            return TeamNode
        if isinstance(instance, Institution):
            return InstitutionNode
        return super().resolve_type(instance, info)


class ContactUnionConnection(relay.Connection):
    class Meta:
        node = ContactUnion
