from django.contrib import admin
from django_extended.admin import ExtendedModelAdmin

from metadatax.bibliography.models import Article, BibliographyType, Conference
from .__form__ import BibliographyForm
from .inlines import AuthorInline


@admin.register(Conference)
class ConferenceAdmin(ExtendedModelAdmin):
    list_display = [
        "title",
        "doi",
        "publication",
        "show_tags",
        "conference_name",
        "conference_location",
        "conference_abstract_book_url",
    ]
    search_fields = [
        "title",
        "doi",
        "conference_name",
    ]
    inlines = [
        AuthorInline,
    ]
    form = BibliographyForm
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "title",
                    "conference_name",
                    "conference_location",
                    "conference_abstract_book_url",
                    "doi",
                    "tags"
                ]
            },
        ),
        (
            "Publication",
            {
                "classes": [
                    "wide",
                ],
                "fields": ["status", "publication_date"],
            },
        ),
    ]

    @admin.display(description='Tags')
    def show_tags(self, obj: Article):
        return self.safe_queryset(obj.tags)

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['conference_name'].required = True
        form.base_fields['conference_location'].required = True
        return form

    def save_model(self, request, obj: Article, form, change):
        obj.type = BibliographyType.CONFERENCE
        super().save_model(request, obj, form, change)
