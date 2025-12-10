from typing import Optional

from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError

from metadatax.common.models import Team, Institution, PersonInstitutionRelation


class PersonInstitutionRelationForm(forms.ModelForm):
    class Meta:
        model = PersonInstitutionRelation
        fields = '__all__'

    def _post_clean(self):
        team: Optional[Team] = self.cleaned_data['team']
        institution: Institution = self.cleaned_data['institution']
        if team is not None and team.institution != institution:
            self.add_error('team', ValidationError("Team should belong to the same institution"))
        super()._post_clean()


class PersonInstitutionRelationInline(admin.TabularInline):
    model = PersonInstitutionRelation
    form = PersonInstitutionRelationForm
    extra = 0
    autocomplete_fields = [
        'institution',
        'team'
    ]
