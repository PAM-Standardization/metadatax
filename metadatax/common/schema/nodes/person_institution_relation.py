import graphene
from django_extension.schema.types import ExtendedNode

from metadatax.common.models import PersonInstitutionRelation
from .institution import InstitutionNode
from .team import TeamNode


class PersonInstitutionRelationNode(ExtendedNode):
    institution = graphene.NonNull(InstitutionNode())
    team = TeamNode()

    class Meta:
        model = PersonInstitutionRelation
        fields = "__all__"
        filter_fields = {
        }
