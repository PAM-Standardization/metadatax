from django import forms
from django.db.models import Choices

from .widgets import AdminAutocompleteSelectWidget


class EnumAutocompleteSelectField(forms.ChoiceField):

    def __init__(self, *, enum: Choices.__class__, **kwargs):
        super().__init__(choices=enum.choices, widget=AdminAutocompleteSelectWidget(choices=enum.choices), **kwargs)
