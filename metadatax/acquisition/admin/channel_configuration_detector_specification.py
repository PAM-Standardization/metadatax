"""Acquisition metadata administration"""

from django.contrib import admin

from metadatax.acquisition.models import ChannelConfigurationDetectorSpecification


@admin.register(ChannelConfigurationDetectorSpecification)
class ChannelConfigurationDetectorSpecificationAdmin(admin.ModelAdmin):
    """ChannelConfigurationDetectorSpecification presentation in DjangoAdmin"""

    list_display = [
        "id",
        "detector",
        "list_output_formats",
        "list_labels",
        "min_frequency",
        "max_frequency",
        "filter",
        "configuration",
    ]
    search_fields = [
        "detector__acoustic_detector_specification__algorithm_name",
        "filter",
        "labels__nickname",
        "labels__source__english_name",
        "labels__sound__english_name",
    ]
    list_filter = [
        "output_formats__name",
    ]

    @admin.display(description="Output formats")
    def list_output_formats(self, obj: ChannelConfigurationDetectorSpecification):
        return ", ".join([f.name for f in obj.output_formats.all()])

    @admin.display(description="Labels")
    def list_labels(self, obj: ChannelConfigurationDetectorSpecification):
        return ", ".join([str(label) for label in obj.labels.all()])
