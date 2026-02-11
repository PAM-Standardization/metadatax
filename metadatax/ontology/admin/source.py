from django.contrib import admin
from django_extension.admin import ExtendedModelAdmin

from metadatax.ontology.models import Source


@admin.register(Source)
class SourceAdmin(ExtendedModelAdmin):
    list_display = [
        "english_name",
        "latin_name",
        "french_name",
        "code_name",
        "taxon",
        "parent",
    ]
    search_fields = [
        "english_name",
        "latin_name",
        "french_name",
        "code_name",
        "taxon",
        "parent__english_name",
    ]
    filter_horizontal = [
        "related_bibliography",
    ]
    autocomplete_fields = [
        "parent",
    ]
