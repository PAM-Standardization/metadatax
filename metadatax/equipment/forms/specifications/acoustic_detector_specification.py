from django import forms

from metadatax.equipment.models import AcousticDetectorSpecification


class AcousticDetectorSpecificationForm(forms.ModelForm):
    class Meta:
        model = AcousticDetectorSpecification
        fields = '__all__'
