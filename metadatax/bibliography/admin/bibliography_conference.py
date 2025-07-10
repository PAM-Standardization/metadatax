from django.contrib import admin

from metadatax.bibliography.models import BibliographyConference


@admin.register(BibliographyConference)
class BibliographyConferenceAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "conference_name",
        "conference_location",
        "conference_abstract_book_url",
    ]
    search_fields = [
        "conference_name",
        "conference_location",
        "conference_abstract_book_url",
    ]
