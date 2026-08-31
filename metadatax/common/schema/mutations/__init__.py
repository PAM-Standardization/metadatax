from graphene import ObjectType

from .institution import InstitutionMutation
from .team import TeamMutation
from .person import CreatePerson
from .contact import ContactMutation


class CommonMutation(ObjectType):
    institution = InstitutionMutation.Field()
    team = TeamMutation.Field()
    create_person = CreatePerson.Field()

    contact = ContactMutation.Field()
