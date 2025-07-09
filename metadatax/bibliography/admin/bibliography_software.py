from django.contrib import admin

from metadatax.bibliography.models import BibliographySoftware


@admin.register(BibliographySoftware)
class BibliographySoftwareAdmin(admin.ModelAdmin):
    list_display = ["id", "publication_place", "repository_url"]
    search_fields = ["publication_place", "repository_url"]
