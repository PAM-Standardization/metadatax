from metadatax.common.models import Person, Institution, Team
from metadatax.common.models.enums import Role
from metadatax.common.models.relations import ContactRelation
from metadatax.utils.forms import ContentTypeModelForm, EnumAutocompleteSelectField, ContentTypeAutocompleteSelectField


class ContactRelationForm(ContentTypeModelForm):
    role = EnumAutocompleteSelectField(enum=Role)

    contact = ContentTypeAutocompleteSelectField(models=[Person, Team, Institution])

    class Meta:
        model = ContactRelation
        fields = ("role", "contact")
        content_type_field_name = 'contact_type'
        object_id_field_name = 'contact_id'
        object_field_name = 'contact'
