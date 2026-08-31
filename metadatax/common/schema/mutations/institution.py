from django import forms
from graphene import Field
from graphene_django.forms.mutation import DjangoModelFormMutation

from metadatax.common.models import Institution
from ..nodes import InstitutionNode


class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = '__all__'


class InstitutionMutation(DjangoModelFormMutation):
    Institution = Field(InstitutionNode)

    class Meta:
        form_class = InstitutionForm
