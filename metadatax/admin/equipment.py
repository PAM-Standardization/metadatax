"""Acquisition metadata administration"""
from django.contrib import admin

from metadatax.models.equipment import (
    Recorder,
    Hydrophone
)


class RecorderAdmin(admin.ModelAdmin):
    """Recorder presentation in DjangoAdmin"""

    search_fields = [
        "provider",
        "model",
        "serial_number",
    ]
    list_filter = [
        "provider",
        "model",
        "number_of_channels"
    ]
    list_display = [
        "id",
        "provider",
        "model",
        "serial_number",
        "number_of_channels",
    ]


class HydrophoneAdmin(admin.ModelAdmin):
    """Hydrophone presentation in DjangoAdmin"""

    search_fields = [
        "provider",
        "model",
        "serial_number",
    ]
    list_filter = [
        "provider",
        "model",
        "directivity"
    ]
    list_display = [
        "id",
        "provider",
        "model",
        "serial_number",
        "sensitivity",
        "directivity",
        "bandwidth",
        "noise_floor",
        "dynamic_range",
        "max_operating_depth",
        "operating_min_temperature",
        "operating_max_temperature",
    ]


admin.site.register(Recorder, RecorderAdmin)
admin.site.register(Hydrophone, HydrophoneAdmin)
