from graphene import ObjectType
from graphene_django_pagination import DjangoPaginationConnectionField

from metadatax.utils.schema import ByIdField
from .nodes import *


class CommonQuery(ObjectType):

    # Person
    all_persons = DjangoPaginationConnectionField(PersonNode)
    person_by_id = ByIdField(PersonNode)

    # Team
    all_teams = DjangoPaginationConnectionField(TeamNode)
    team_by_id = ByIdField(TeamNode)

    # Institution
    all_institutions = DjangoPaginationConnectionField(InstitutionNode)
    institution_by_id = ByIdField(InstitutionNode)
