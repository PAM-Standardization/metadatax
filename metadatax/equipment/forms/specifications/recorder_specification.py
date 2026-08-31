from django import forms

from metadatax.equipment.models import RecorderSpecification


class RecorderSpecificationForm(forms.ModelForm):
    class Meta:
        model = RecorderSpecification
        fields = '__all__'


