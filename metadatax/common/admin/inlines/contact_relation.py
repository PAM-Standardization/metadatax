from django.contrib import admin
from django_extended.forms import ContentTypeModelForm
from django_extended.forms.fields import EnumAutocompleteSelectField, ContentTypeAutocompleteSelectField

from metadatax.common.models import Role, Person, Team, Institution, ContactRelation


class ContactRelationForm(ContentTypeModelForm):
    # TODO!!
    role = EnumAutocompleteSelectField(enum=Role)

    contact = ContentTypeAutocompleteSelectField(models=[Person, Team, Institution])

    class Meta:
        model = ContactRelation
        fields = ("role", "contact")
        content_type_field_name = 'contact_type'
        object_id_field_name = 'contact_id'
        object_field_name = 'contact'


class ContactRelationInline(admin.TabularInline):
    model = ContactRelation
    form = ContactRelationForm
    extra = 0
