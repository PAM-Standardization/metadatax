from django.contrib import admin
from django.utils.html import format_html
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django_extended.admin import JSONExportModelAdmin

from metadatax.ontology.models import Label
from metadatax.ontology.serializers import LabelSerializer


@admin.register(Label)
class LabelAdmin(JSONExportModelAdmin, DynamicArrayMixin):
    depth = 1
    model = Label
    serializer = LabelSerializer

    list_display = [
        "__str__",
        "source",
        "sound",
        "nickname",
        "associated_names",
        "parent",
        "shape",
        "plurality",
        "show_frequencies",
        "show_mean_duration",
    ]
    search_fields = [
        "source__english_name",
        "source__latin_name",
        "source__french_name",
        "source__code_name",
        "source__taxon",
        "sound__english_name",
        "sound__french_name",
        "sound__code_name",
        "sound__taxon",
        "nickname",
        "parent__nickname",
        "parent__source__english_name",
        "parent__sound__english_name",
        "associated_names",
    ]
    list_filter = [
        "shape",
        "plurality",
    ]
    filter_horizontal = [
        "related_bibliography",
    ]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "source",
                    "sound",
                    "nickname",
                    "associated_names",
                    "related_bibliography",
                ]
            },
        ),
        (
            "Physical description",
            {
                "classes": [
                    "wide",
                ],
                "fields": [
                    "shape",
                    "plurality",
                    "min_frequency",
                    "max_frequency",
                    "mean_duration",
                    "description",
                ],
            },
        ),
    ]

    @admin.display(description="Frequencies (in Hz)")
    def show_frequencies(self, label: Label):
        return format_html(
            f"""
            min: {label.min_frequency or "-"}
            <br/>
            max: {label.max_frequency or "-"}
        """
        )

    @admin.display(description="Mean duration (in s)")
    def show_mean_duration(self, label: Label):
        return label.mean_duration
