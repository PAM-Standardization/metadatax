"""Acquisition metadata administration"""
from django.contrib import admin

from metadatax.models.data import (
    File,
)
from .__util__ import custom_titled_filter


class FileAdmin(admin.ModelAdmin):
    """File presentation in DjangoAdmin"""

    search_fields = [
        "channel_configuration__channel_name",
    ]
    list_filter = [
        "accessibility",
        "format",
        ("channel_configuration__hydrophone__model", custom_titled_filter("hydrophone model")),
        ("channel_configuration__recorder__model", custom_titled_filter("recorder model")),

    ]
    list_display = [
        "name",
        "format",
        "channel_configuration",
        "initial_timestamp",
        "duration",
        "sampling_frequency",
        "sample_depth",
        "storage_location",
        "bit_counts",
    ]


admin.site.register(File, FileAdmin)
