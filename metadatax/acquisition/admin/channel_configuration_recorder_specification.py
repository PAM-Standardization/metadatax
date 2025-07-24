"""Acquisition metadata administration"""
from django.contrib import admin

from metadatax.acquisition.models import ChannelConfigurationRecorderSpecification


@admin.register(ChannelConfigurationRecorderSpecification)
class ChannelConfigurationRecorderSpecificationAdmin(admin.ModelAdmin):
    """ChannelConfigurationRecorderSpecification presentation in DjangoAdmin"""

    list_display = [
        "id",
        "recorder",
        "hydrophone",
        "list_recording_formats",
        "sampling_frequency",
        "sample_depth",
        "gain",
        "channel_name",
    ]
    search_fields = [
        "channel_name",
        "recorder__model",
        "recorder__name",
        "recorder__provider__name",
        "hydrophone__model",
        "hydrophone__name",
        "hydrophone__provider__name",
        "recording_formats__name",
        "sampling_frequency",
        "sample_depth",
        "gain",
        "channel_name",
    ]
    list_filter = [
        "recording_formats__name",
    ]
    autocomplete_fields = [
        "recorder",
        "hydrophone",
        "recording_formats",
    ]

    @admin.display(description="Output formats")
    def list_recording_formats(self, obj: ChannelConfigurationRecorderSpecification):
        return ", ".join([f.name for f in obj.recording_formats.all()])
