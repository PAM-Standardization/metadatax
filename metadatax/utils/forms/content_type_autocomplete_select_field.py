from django import forms
from django.db.models import Model

from metadatax.utils.forms.widgets import AdminAutocompleteSelectWidget


class ContentTypeAutocompleteSelectField(forms.ChoiceField):

    def __init__(self, *,
                 models: [Model.__class__],
                 **kwargs):
        choices = [("-", "---")] + [
            (
                f"{m._meta.app_label}.{m._meta.model_name}--{o.pk}",  # Value
                f"{m.__name__}: {str(o)}"  # Label
            )
            for m in models
            for o in m.objects.all()
        ]
        super().__init__(choices=choices, widget=AdminAutocompleteSelectWidget(choices=choices), **kwargs)

    def clean(self, value):
        return super().clean(value)

