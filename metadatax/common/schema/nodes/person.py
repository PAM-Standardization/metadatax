import graphene
import graphene_django_optimizer
from graphene import relay, ID

from metadatax.common.models import Person
from metadatax.utils.schema import MxObjectType
from .relations import PersonInstitutionRelationNode


class PersonNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = Person
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "first_name": ["exact", "icontains"],
            "last_name": ["exact", "icontains"],
            "mail": ["exact", "icontains"],
            "website": ["exact", "icontains"],
        }
        interfaces = (relay.Node,)

    institution_relations = graphene.List(PersonInstitutionRelationNode)

    @graphene_django_optimizer.resolver_hints()
    def resolve_institution_relations(self: Person, info):
        """Resolve institution_relations"""
        return self.institution_relations.all()

