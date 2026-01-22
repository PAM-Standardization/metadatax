from django.contrib import admin
from django_extension.admin import ExtendedModelAdmin

from metadatax.common.models import Person
from .inlines import PersonInstitutionRelationInline


@admin.register(Person)
class PersonAdmin(ExtendedModelAdmin):
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
        return self.list_queryset(
            obj.institution_relations.all(),
            to_str=lambda rel: f"{rel.institution} ({rel.team.name})" if rel.team else rel.institution
        )
