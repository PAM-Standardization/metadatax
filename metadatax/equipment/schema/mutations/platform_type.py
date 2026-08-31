from django import forms
from graphene import Field
from graphene_django.forms.mutation import DjangoModelFormMutation

from metadatax.equipment.models import PlatformType
from ..nodes import PlatformTypeNode


class PlatformTypeForm(forms.ModelForm):
    class Meta:
        model = PlatformType
        fields = '__all__'


class PlatformTypeMutation(DjangoModelFormMutation):
    PlatformType = Field(PlatformTypeNode)

    class Meta:
        form_class = PlatformTypeForm
