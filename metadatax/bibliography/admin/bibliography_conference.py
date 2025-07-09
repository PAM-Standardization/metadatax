from django.contrib import admin
from django.db import models


class BibliographyConference(models.Model):
    conference_name = models.CharField(
        max_length=255, help_text="Required for a conference"
    )
    conference_location = models.CharField(
        max_length=255,
        help_text="Required for a conference (format: {City}, {Country})",
    )
    conference_abstract_book_url = models.URLField(null=True, blank=True)


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
