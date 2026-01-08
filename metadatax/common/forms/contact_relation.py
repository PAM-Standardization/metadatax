from django.contrib.contenttypes.models import ContentType
from django import forms
from django.forms.utils import ErrorList
from django_extended.forms.fields import EnumAutocompleteSelectField, ContentTypeAutocompleteSelectField

from metadatax.common.models import Role, Institution, Team, ContactRelation, Person


class ContactRelationForm(forms.ModelForm):
    role = EnumAutocompleteSelectField(enum=Role)
    contact = ContentTypeAutocompleteSelectField(models=[Person, Team, Institution])

    class Meta:
        abstract = True

    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None):
        if instance is not None:
            initial = {
                "role": instance.contactrelation.role,
                "contact": instance.contactrelation.contact,
            }
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance,
                         use_required_attribute, renderer)

    def save(self, commit=True):
        self.instance.contactrelation = ContactRelation.objects.get_or_create(
            role=self.cleaned_data['role'],
            contact_type=ContentType.objects.get_for_model(self.cleaned_data['contact']),
            contact_id=self.cleaned_data['contact'].pk
        )[0]

        return super().save(commit)
