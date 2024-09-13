"""Acquisition metadata administration"""
from django.contrib import admin

from metadatax.models.data import File
from .__util__ import custom_titled_filter, JSONExportModelAdmin
from ..models import Accessibility


@admin.register(File)
class FileModelAdmin(JSONExportModelAdmin):
    """File presentation in DjangoAdmin"""

    model = File
    depth = 5

    search_fields = [
        "channel_configuration__channel_name",
    ]
    list_filter = [
        "accessibility",
        "format",
        (
            "channel_configuration__hydrophone__model",
            custom_titled_filter("hydrophone model"),
        ),
        (
            "channel_configuration__recorder__model",
            custom_titled_filter("recorder model"),
        ),
    ]
    list_display = [
        "name",
        "format",
        "channel_configuration",
        "get_accessibility",
        "initial_timestamp",
        "duration",
        "sampling_frequency",
        "sample_depth",
        "storage_location",
        "file_size",
    ]

    @admin.display(description="Accessibility")
    def get_accessibility(self, obj):
        if obj.accessibility is not None:
            accessibility = obj.accessibility
        else:
            accessibility = obj.channel_configuration.deployment.project.accessibility
        for choices in Accessibility.choices:
            if choices[0] == accessibility:
                return choices[1]
        return accessibility
