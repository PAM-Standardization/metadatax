from django import forms
from django_extension.schema.mutations import ModelDeleteMutation, ExtendedModelFormMutation

from metadatax.ontology.models import Sound


class SoundForm(forms.ModelForm):
    class Meta:
        model = Sound
        exclude = ('related_bibliography',)


class PostSoundMutation(ExtendedModelFormMutation):
    class Meta:
        model = Sound
        form_class=SoundForm


class DeleteSoundMutation(ModelDeleteMutation):
    class Meta:
        model_class = Sound
