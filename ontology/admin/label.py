from django.contrib import admin

from ontology.models import Label
from ontology.serializers import LabelSerializer
from utils.admin import JSONExportModelAdmin


@admin.register(Label)
class LabelAdmin(JSONExportModelAdmin):
    depth = 1
    model = Label
    serializer = LabelSerializer

    list_display = [
        "source",
        "sound",
        "nickname",
        "show_shape",
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
    list_filter = ["physical_descriptor__shape", "physical_descriptor__plurality"]

    @admin.display(description="Shape")
    def show_shape(self, label: Label):
        if label.physical_descriptor is None:
            return ""
        return (
            f"{label.physical_descriptor.shape} - {label.physical_descriptor.plurality}"
        )

    @admin.display(description="Frequencies")
    def show_frequencies(self, label: Label):
        if label.physical_descriptor is None:
            return ""
        return f"{label.physical_descriptor.min_frequency} < {label.physical_descriptor.max_frequency}"

    @admin.display(description="Mean duration")
    def show_mean_duration(self, label: Label):
        if label.physical_descriptor is None:
            return ""
        return label.physical_descriptor.mean_duration
