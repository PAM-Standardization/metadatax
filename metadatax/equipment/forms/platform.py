from typing import Optional

from django import forms
from django.contrib.contenttypes.models import ContentType
from django.forms.utils import ErrorList
from django_extended.forms.fields import ContentTypeAutocompleteSelectField

from metadatax.common.models import Person, Team, Institution
from metadatax.equipment.models import Platform


class PlatformForm(forms.ModelForm):
    # Additional typing
    instance: Optional[Platform]

    class Meta:
        model = Platform
        exclude = ("owner_type", "owner_id")

    owner = ContentTypeAutocompleteSelectField(models=[Person, Team, Institution])

    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None):
        if instance is not None:
            initial = {
                "owner": instance.owner,
            }
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance,
                         use_required_attribute, renderer)

    def save(self, commit=True):
        self.instance.owner_type = ContentType.objects.get_for_model(self.cleaned_data['owner'])
        self.instance.owner_id = self.cleaned_data['owner'].pk

        return super().save(commit)
