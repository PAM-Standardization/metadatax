from django.contrib import admin
from django.utils.html import format_html
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django_extension.admin import ExtendedModelAdmin

from metadatax.ontology.models import Label, LabelDisplay
from metadatax.ontology.serializers import LabelSerializer


@admin.register(Label)
class LabelAdmin(ExtendedModelAdmin, DynamicArrayMixin):
    actions = ["export", ]
    depth = 1
    serializer = LabelSerializer

    list_display = [
        "english_name",
        "french_name",
        "code_name",
        "source",
        "sound",
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

    @admin.display(description="English name")
    def english_name(self, label: Label):
        return label.display(LabelDisplay.ENGLISH)

    @admin.display(description="French name")
    def french_name(self, label: Label):
        return label.display(LabelDisplay.FRENCH)

    @admin.display(description="Code name")
    def code_name(self, label: Label):
        return label.display(LabelDisplay.CODE)
