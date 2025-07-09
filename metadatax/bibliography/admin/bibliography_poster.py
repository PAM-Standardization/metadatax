from django.contrib import admin

from metadatax.bibliography.models import BibliographyPoster


@admin.register(BibliographyPoster)
class BibliographyPosterAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "poster_url",
    ]
    search_fields = [
        "poster_url",
    ]
