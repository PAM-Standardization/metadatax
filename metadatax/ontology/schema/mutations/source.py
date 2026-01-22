from django import forms
from django_extension.schema.mutations import ModelDeleteMutation, ExtendedModelFormMutation

from metadatax.ontology.models import Source


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        exclude = ('related_bibliography',)


class PostSourceMutation(ExtendedModelFormMutation):
    class Meta:
        model = Source
        form_class = SourceForm


class DeleteSourceMutation(ModelDeleteMutation):
    class Meta:
        model_class = Source
