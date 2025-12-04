import graphene
from graphene import relay

from metadatax.common.models.relations import PersonInstitutionRelation
from metadatax.common.schema.nodes import TeamNode, InstitutionNode
from metadatax.utils.schema import MxObjectType


class PersonInstitutionRelationNode(MxObjectType):

    institution = graphene.NonNull(InstitutionNode())
    team = TeamNode()

    class Meta:
        model = PersonInstitutionRelation
        fields = "__all__"
        filter_fields = {
        }
        interfaces = (relay.Node,)
