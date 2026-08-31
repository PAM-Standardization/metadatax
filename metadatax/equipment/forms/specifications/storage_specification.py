from django import forms

from metadatax.equipment.models import StorageSpecification


class StorageSpecificationForm(forms.ModelForm):
    class Meta:
        model = StorageSpecification
        fields = '__all__'
