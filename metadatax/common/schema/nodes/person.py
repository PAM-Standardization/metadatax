import graphene
import graphene_django_optimizer
from django_extension.schema.types import ExtendedNode

from metadatax.common.models import Person
from .person_institution_relation import PersonInstitutionRelationNode


class PersonNode(ExtendedNode):
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

    institution_relations = graphene.List(PersonInstitutionRelationNode)

    @graphene_django_optimizer.resolver_hints()
    def resolve_institution_relations(self: Person, info):
        """Resolve institution_relations"""
        return self.institution_relations.all()
