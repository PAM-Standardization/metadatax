"""Acquisition metadata administration"""
from django.contrib import admin

from metadatax.models.equipment import (
    Recorder,
    Hydrophone, EquipmentProvider, RecorderModel, HydrophoneModel, HydrophoneDirectivity
)


@admin.register(EquipmentProvider)
class EquipmentProviderAdmin(admin.ModelAdmin):
    search_fields = [
        "name",
    ]
    list_display = [
        "name",
        "contact",
        "website",
    ]


@admin.register(RecorderModel)
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


@admin.register(Recorder)
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


@admin.register(HydrophoneModel)
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
        "bandwidth",
        "noise_floor",
        "dynamic_range",
        "max_operating_depth"
    ]


@admin.register(Hydrophone)
class HydrophoneAdmin(admin.ModelAdmin):
    """Hydrophone presentation in DjangoAdmin"""

    search_fields = [
        "model",
        "serial_number",
    ]
    list_filter = [
        "model__provider",
        "model__directivity",
    ]
    list_display = [
        "serial_number",
        "model",
        "sensitivity",
        "directivity",
        "operating_temperature",
        "bandwidth",
        "noise_floor",
        "dynamic_range",
        "max_operating_depth"
    ]

    def directivity(self, obj):
        for choices in HydrophoneDirectivity.choices:
            if choices[0] == obj.model.directivity:
                return choices[1]
        return obj.model.directivity

    def operating_temperature(self, obj):
        return obj.model.operating_temperature()

    def bandwidth(self, obj):
        return obj.model.bandwidth()

    def dynamic_range(self, obj):
        return obj.model.dynamic_range()

    def noise_floor(self, obj):
        return obj.model.noise_floor

    def max_operating_depth(self, obj):
        return obj.model.max_operating_depth
