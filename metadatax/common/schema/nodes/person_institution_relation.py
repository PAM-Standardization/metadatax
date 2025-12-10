from django_extended.schema.interfaces import ExtendedInterface
from django_extended.schema.types import ExtendedNode
import graphene

from metadatax.common.models import PersonInstitutionRelation
from .team import TeamNode
from .institution import InstitutionNode


class PersonInstitutionRelationNode(ExtendedNode):
    institution = graphene.NonNull(InstitutionNode())
    team = TeamNode()

    class Meta:
        model = PersonInstitutionRelation
        fields = "__all__"
        filter_fields = {
        }
        interfaces = (ExtendedInterface,)
