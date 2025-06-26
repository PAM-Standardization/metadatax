from django.contrib import admin

from metadatax_equipment.models import AcousticDetectorSpecification


@admin.register(AcousticDetectorSpecification)
class AcousticDetectorSpecificationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "show_labels",
        "min_frequency",
        "algorithm_name",
    ]
    search_fields = [
        "detected_labels__nickname",
        "detected_labels__source__english_name",
        "detected_labels__sound__english_name",
        "algorithm_name"
    ]

    @admin.display(description="Detected labels")
    def show_labels(self, instance: AcousticDetectorSpecification):
        return ', '.join([
            str(label) for label in instance.detected_labels.all()
        ])
