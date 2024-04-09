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


admin.site.register(Recorder, RecorderAdmin)
admin.site.register(Hydrophone, HydrophoneAdmin)
