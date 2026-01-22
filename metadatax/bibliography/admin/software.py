from django.contrib import admin
from django_extension.admin import ExtendedModelAdmin

from metadatax.bibliography.models import Article, BibliographyType, Software
from .__form__ import BibliographyForm
from .inlines import AuthorInline


@admin.register(Software)
class SoftwareAdmin(ExtendedModelAdmin):
    list_display = [
        "title",
        "doi",
        "publication",
        "show_tags",
        "publication_place",
        "repository_url",
    ]
    search_fields = [
        "title",
        "doi",
        "publication_place",
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
                    "publication_place",
                    "repository_url",
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
        form.base_fields['publication_place'].required = True
        return form

    def save_model(self, request, obj: Article, form, change):
        obj.type = BibliographyType.SOFTWARE
        super().save_model(request, obj, form, change)
