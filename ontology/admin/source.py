from django.contrib import admin

from ontology.models import Source


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):

    list_display = [
        "english_name",
        "latin_name",
        "french_name",
        "code_name",
        "taxon",
        "parent"
    ]
    search_fields = [
        "english_name",
        "latin_name",
        "french_name",
        "code_name",
        "taxon",
    ]
