from typing import Optional

from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError

from metadatax.bibliography.models import Bibliography
from .author import AuthorInline
from ...utils.admin import get_many_to_many


class BibliographyForm(forms.ModelForm):
    status = forms.ChoiceField(
        choices=Bibliography.Status.choices, widget=forms.RadioSelect
    )
    type = forms.ChoiceField(
        choices=Bibliography.Type.choices, widget=forms.RadioSelect
    )

    class Meta:
        model = Bibliography
        fields = "__all__"

    def _check_field_empty(
        self, biblio_type: Bibliography.Type, field_name: str, should_be_empty: bool
    ):
        data = self.cleaned_data.get(field_name)
        if should_be_empty and data is not None:
            raise ValidationError(
                {
                    field_name: f"This {field_name} should stay empty for a '{biblio_type.label}' type bibliography."
                }
            )

    def clean(self):
        super().clean()

        status: Optional[Bibliography.Status] = self.cleaned_data.get("status")
        if status is not None:
            if (
                status == Bibliography.Status.PUBLISHED
                and self.cleaned_data.get("publication_date") is None
            ):
                raise ValidationError(
                    {
                        "publication_date": "This custom_fields is required for a 'Published' bibliography."
                    }
                )

        b_type: Optional[Bibliography.Type] = self.cleaned_data.get("type")
        if b_type is not None:
            self._check_field_empty(
                b_type, "software_information", should_be_empty=b_type!=Bibliography.Type.SOFTWARE
            )
            self._check_field_empty(
                b_type, "article_information", should_be_empty=b_type!=Bibliography.Type.ARTICLE
            )
            self._check_field_empty(
                b_type, "conference_information", should_be_empty=b_type!=Bibliography.Type.CONFERENCE and b_type!=Bibliography.Type.POSTER
            )
            self._check_field_empty(
                b_type, "poster_information", should_be_empty=b_type!=Bibliography.Type.POSTER
            )

        return self.cleaned_data


@admin.register(Bibliography)
class BibliographyAdmin(admin.ModelAdmin):
    """Collaborator presentation in DjangoAdmin"""

    list_display = ["title", "doi", "publication", "type", "show_tags"]
    search_fields = [
        "title",
        "doi",
    ]
    filter_horizontal = ("tags",)
    inlines = [
        AuthorInline,
    ]
    form = BibliographyForm
    fieldsets = [
        (
            None,
            {"fields": ["title", "doi", "tags"]},
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
        (
            "Type",
            {
                "classes": [
                    "wide",
                ],
                "fields": [
                    "type",
                    "software_information",
                    "article_information",
                    "conference_information",
                    "poster_information",
                ],
            },
        ),
    ]
    autocomplete_fields = [
        "software_information",
        "article_information",
        "conference_information",
        "poster_information",
    ]

    @admin.display(description="Tags")
    def show_tags(self, obj: Bibliography):
        """show_tags"""
        return get_many_to_many(obj, "tags", "name")
