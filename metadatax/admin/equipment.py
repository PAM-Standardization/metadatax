"""Acquisition metadata administration"""
from django.contrib import admin

from metadatax.models.equipment import (
    Recorder,
    Hydrophone, EquipmentProvider, RecorderModel, HydrophoneModel
)


class EquipmentProviderAdmin(admin.ModelAdmin):
    search_fields = [
        "name",
    ]
    list_display = [
        "name",
        "contact",
        "website",
    ]


class RecorderModelAdmin(admin.ModelAdmin):
    search_fields = [
        "name",
        "provider",
    ]
    list_filter = [
        "number_of_channels"
    ]
    list_display = [
        "name",
        "provider",
        "number_of_channels",
    ]


class RecorderAdmin(admin.ModelAdmin):
    """Recorder presentation in DjangoAdmin"""

    search_fields = [
        "model",
        "serial_number",
    ]
    list_filter = [
        "model__provider",
        "model__number_of_channels",
    ]
    list_display = [
        "serial_number",
        "model",
        "number_of_channels",
    ]

    def number_of_channels(self, obj):
        return obj.model.number_of_channels


class HydrophoneModelAdmin(admin.ModelAdmin):
    search_fields = [
        "name",
        "provider",
    ]
    list_filter = [
        "directivity"
    ]
    list_display = [
        "name",
        "provider",
        "directivity",
        "operating_temperature",
    ]


class HydrophoneAdmin(admin.ModelAdmin):
    """Hydrophone presentation in DjangoAdmin"""

    search_fields = [
        "model",
        "serial_number",
    ]
    list_filter = [
        "model__provider",
    ]
    list_display = [
        "serial_number",
        "model",
        "sensitivity",
        "bandwidth",
        "noise_floor",
        "dynamic_range",
        "max_operating_depth",
        "operating_temperature",
    ]

    def operating_temperature(self, obj):
        return obj.model.operating_temperature()


admin.site.register(EquipmentProvider, EquipmentProviderAdmin)
admin.site.register(RecorderModel, RecorderModelAdmin)
admin.site.register(Recorder, RecorderAdmin)
admin.site.register(HydrophoneModel, HydrophoneModelAdmin)
admin.site.register(Hydrophone, HydrophoneAdmin)
