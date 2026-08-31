from django import forms

from metadatax.equipment.models import HydrophoneSpecification


class HydrophoneSpecificationForm(forms.ModelForm):
    class Meta:
        model = HydrophoneSpecification
        fields = '__all__'
