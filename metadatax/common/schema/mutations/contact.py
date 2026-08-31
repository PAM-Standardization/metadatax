from django import forms
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
import graphene
from graphene import Field
from graphene_django.types import ErrorType

from metadatax.common.models import ContactRelation
from ..enums import RoleEnum, ContactTypeEnum
from ..nodes import ContactRelationNode


class ContactInput(graphene.InputObjectType):
    role = graphene.NonNull(RoleEnum)
    contact_type = graphene.NonNull(ContactTypeEnum)
    contact_id = graphene.NonNull(graphene.ID)


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRelation
        fields = '__all__'


class ContactMutation(graphene.Mutation):
    class Arguments:
        contact = graphene.NonNull(ContactInput)

    contact = Field(ContactRelationNode)
    errors = graphene.List(ErrorType)

    @classmethod
    @transaction.atomic
    def mutate(cls, root, info, input):
        errors = []

        input['role'] = input['role'].value
        input['contact_type'] = ContentType.objects.get(
            app_label="common",
            model=input.pop('contact_type').value,
        ).id

        form = ContactForm(data=input)
        if form.is_valid():
            return cls(contact=form.save())
        else:
            return cls(errors=[
                ErrorType(field=field, messages=messages)
                for field, messages in form.errors.items()
            ])
