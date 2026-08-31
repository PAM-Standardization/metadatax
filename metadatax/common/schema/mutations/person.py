from django import forms
from django.db import transaction
import graphene
from graphene_django.types import ErrorType

from metadatax.common.models import Person
from metadatax.common.forms import PersonInstitutionRelationForm
from ..nodes import PersonNode


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ('teams', 'institutions',)


class PersonInstitutionRelationInput(graphene.InputObjectType):
    """Input for a single Person <-> Institution relation."""

    institution = graphene.ID(required=True)
    team = graphene.ID(required=False)
    from_date = graphene.Date(required=False)
    to_date = graphene.Date(required=False)


class PersonInput(graphene.InputObjectType):
    """Input for creating a Person, including its institution relations."""

    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    mail = graphene.String(required=False)
    website = graphene.String(required=False)
    institution_relations = graphene.List(
        PersonInstitutionRelationInput, required=False
    )


class CreatePerson(graphene.Mutation):
    """Create a Person along with its institution/team relations."""

    class Arguments:
        input = PersonInput(required=True)

    person = graphene.Field(PersonNode)
    errors = graphene.List(ErrorType)

    @classmethod
    @transaction.atomic
    def mutate(cls, root, info, input):
        relations_data = input.pop("institution_relations", []) or []

        # Reuse the ModelForm for validation of the simple Person fields
        form = PersonForm(data=dict(input))

        if not form.is_valid():
            errors = [
                ErrorType(field=field, messages=messages)
                for field, messages in form.errors.items()
            ]
            return cls(person=None, errors=errors)

        person = form.save()
        errors = []

        for index in range(0, len(relations_data)):
            relation_form = PersonInstitutionRelationForm(data={
                "person": person,
                "institution": relations_data[index]["institution"],
                **relations_data[index]
            })
            if not relation_form.is_valid():
                for field, messages in relation_form.errors.items():
                    errors.append(ErrorType(field=f"institution_relations-{index}-{field}", messages=messages))
                relation_form.save()

        return cls(person=person, errors=[])
