from typing import Optional

from django import forms
from django.core.exceptions import ValidationError

from metadatax.common.models import Team, Institution
from metadatax.common.models.relations import PersonInstitutionRelation


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

    def save(self, commit=True):
        return super().save(commit)