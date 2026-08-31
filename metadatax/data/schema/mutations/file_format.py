from django import forms
from graphene import Field
from graphene_django.forms.mutation import DjangoModelFormMutation

from metadatax.data.models import FileFormat
from ..nodes import FileFormatNode


class FileFormatForm(forms.ModelForm):
    class Meta:
        model = FileFormat
        fields = '__all__'


class FileFormatMutation(DjangoModelFormMutation):
    FileFormat = Field(FileFormatNode)

    class Meta:
        form_class = FileFormatForm
