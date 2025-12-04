from django.contrib import admin

from metadatax.common.forms.relations import PersonInstitutionRelationForm
from metadatax.common.models.relations import PersonInstitutionRelation


class PersonInstitutionRelationInline(admin.TabularInline):
    model = PersonInstitutionRelation
    form = PersonInstitutionRelationForm
    extra = 0
    autocomplete_fields = [
        'institution',
        'team'
    ]
