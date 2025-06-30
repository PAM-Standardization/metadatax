from django.contrib import admin

from metadatax.ontology.models import Sound


@admin.register(Sound)
class SoundAdmin(admin.ModelAdmin):
    list_display = ["english_name", "french_name", "code_name", "taxon", "parent"]
    search_fields = [
        "english_name",
        "french_name",
        "code_name",
        "taxon",
    ]
