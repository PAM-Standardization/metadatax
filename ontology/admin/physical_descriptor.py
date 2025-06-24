from django.contrib import admin

from ontology.models import PhysicalDescriptor


@admin.register(PhysicalDescriptor)
class PhysicalDescriptorAdmin(admin.ModelAdmin):
    list_display = [
        "label",
        "shape",
        "plurality",
        "show_frequencies",
        "mean_duration",
        "description",
    ]
    search_fields = [
        "description",
        "label__source__english_name",
        "label__source__latin_name",
        "label__source__french_name",
        "label__source__code_name",
        "label__source__taxon",
        "label__sound__english_name",
        "label__sound__french_name",
        "label__sound__code_name",
        "label__sound__taxon",
    ]
    list_filter = ["shape", "plurality"]

    @admin.display(description="Frequencies")
    def show_frequencies(self, descriptor: PhysicalDescriptor):
        return f"{descriptor.min_frequency} < {descriptor.max_frequency}"
