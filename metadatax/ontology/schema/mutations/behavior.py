from django import forms
from django_extension.schema.mutations import ExtendedModelFormMutation

from metadatax.ontology.models import Behavior


class BehaviorForm(forms.ModelForm):
    class Meta:
        model = Behavior
        fields = '__all__'


class BehaviorMutation(ExtendedModelFormMutation):
    class Meta:
        model = Behavior
        form_class = BehaviorForm
