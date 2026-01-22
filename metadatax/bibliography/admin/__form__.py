from django.core.exceptions import ValidationError
from django_extension.forms import ExtendedForm

from metadatax.common.forms import TaggedItemForm
from metadatax.bibliography.models import Bibliography, BibliographyStatus


class BibliographyForm(TaggedItemForm, ExtendedForm):
    class Meta:
        model = Bibliography
        fields = '__all__'

    def clean(self):
        data = super().clean()
        if data['status'] == BibliographyStatus.PUBLISHED and data[
            'publication_date'] is None:
            raise ValidationError('Cannot publish without a publication date')
        return data
