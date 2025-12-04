from django.contrib import admin
from django.utils.safestring import mark_safe

from metadatax.common.models import Person
from .relations import PersonInstitutionRelationInline


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Person administration"""

    list_display = [
        "initial_names",
        "first_name",
        "last_name",
        "mail",
        "website",
        "institutions_list",
    ]
    search_fields = [
        "first_name",
        "last_name",
        "mail",
        "website",
        "institutions__name",
        "teams__name",
    ]
    list_filter = [
        "institutions"
    ]
    filter_horizontal = [
        "institutions",
    ]
    inlines = [
        PersonInstitutionRelationInline,
    ]

    @admin.display(description="Institutions")
    def institutions_list(self, obj: Person) -> str:
        """Display readable information about institutions"""
        print(obj.institution_relations)
        return mark_safe("<br/>".join([
            f"{rel.institution} ({rel.team.name})" if rel.team else rel.institution
            for rel in obj.institution_relations.all()
        ]))

