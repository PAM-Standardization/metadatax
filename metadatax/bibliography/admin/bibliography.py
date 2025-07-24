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
                    field_name: f"This custom_fields should stay empty for a '{biblio_type.label}' type bibliography."
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
            t = Bibliography.Type

            self._check_field_empty(
                t.SOFTWARE, "software_information", should_be_empty=False
            )
            self._check_field_empty(
                t.SOFTWARE, "article_information", should_be_empty=True
            )
            self._check_field_empty(
                t.SOFTWARE, "conference_information", should_be_empty=True
            )
            self._check_field_empty(
                t.SOFTWARE, "poster_information", should_be_empty=True
            )

            self._check_field_empty(
                t.ARTICLE, "software_information", should_be_empty=True
            )
            self._check_field_empty(
                t.ARTICLE, "article_information", should_be_empty=False
            )
            self._check_field_empty(
                t.ARTICLE, "conference_information", should_be_empty=True
            )
            self._check_field_empty(
                t.ARTICLE, "poster_information", should_be_empty=True
            )

            self._check_field_empty(
                t.CONFERENCE, "software_information", should_be_empty=True
            )
            self._check_field_empty(
                t.CONFERENCE, "article_information", should_be_empty=True
            )
            self._check_field_empty(
                t.CONFERENCE, "conference_information", should_be_empty=False
            )
            self._check_field_empty(
                t.CONFERENCE, "poster_information", should_be_empty=True
            )

            self._check_field_empty(
                t.POSTER, "software_information", should_be_empty=True
            )
            self._check_field_empty(
                t.POSTER, "article_information", should_be_empty=True
            )
            self._check_field_empty(
                t.POSTER, "poster_information", should_be_empty=False
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
