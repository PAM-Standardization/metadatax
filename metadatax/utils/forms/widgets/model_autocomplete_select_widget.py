import json

from django import forms
from django.contrib.admin.widgets import AutocompleteSelect
from django.db import models

from admin.site import MetadataxAdminSite


class AdminModelAutocompleteSelectWidget(AutocompleteSelect):


    def __init__(self, model: models.Model.__class__, field_name: str, attrs=None):
        self.model = model
        self.field_name = field_name
        super().__init__(forms.ModelChoiceField(queryset=model.objects.all()), MetadataxAdminSite(), attrs)

    # def optgroups(self, name, value, attr=None):
    #     """Return selected options based on the ModelChoiceIterator."""
    #     self.choices = self.field._get_choices()
    #     default = (None, [], 0)
    #     groups = [default]
    #     has_selected = False
    #     selected_choices = {
    #         str(v) for v in value
    #         if str(v) not in self.choices.field.empty_values
    #     }
    #     if not self.is_required and not self.allow_multiple_selected:
    #         default[1].append(self.create_option(name, '', '', False, 0))
    #     choices = (
    #         (obj.pk, self.choices.field.label_from_instance(obj))
    #         for obj in self.choices.queryset.using(self.db).filter(pk__in=selected_choices)
    #     )
    #     for option_value, option_label in choices:
    #         selected = (
    #                 str(option_value) in value and
    #                 (has_selected is False or self.allow_multiple_selected)
    #         )
    #         has_selected |= selected
    #         index = len(default[1])
    #         subgroup = default[1]
    #         subgroup.append(self.create_option(name, option_value, option_label, selected_choices, index))
    #     return groups
    #
    # def build_attrs(self, base_attrs, extra_attrs=None):
    #     """
    #     Set select2's AJAX attributes.
    #
    #     Attributes can be set using the html5 data attribute.
    #     Nested attributes require a double dash as per
    #     https://select2.org/configuration/data-attributes#nested-subkey-options
    #     """
    #     attrs = super(forms.Select, self).build_attrs(base_attrs, extra_attrs=extra_attrs)
    #     attrs.setdefault('class', '')
    #     attrs.update({
    #         # 'data-ajax--cache': 'true',
    #         # 'data-ajax--delay': 250,
    #         # 'data-ajax--type': 'GET',
    #         # 'data-ajax--url': self.get_url(), # TODO: Update MetadataxAdminSite.autocomplete_view
    #         # 'data-app-label': self.model._meta.app_label,
    #         # 'data-model-name': self.model._meta.model_name,
    #         # 'data-field-name': 'name',
    #         'data-theme': 'admin-autocomplete',
    #         'data-allow-clear': json.dumps(not self.is_required),
    #         'data-placeholder': '',  # Allows clearing of the input.
    #         'class': attrs['class'] + (' ' if attrs['class'] else '') + 'admin-autocomplete',
    #     })
    #     return attrs



