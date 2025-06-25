from django.contrib import admin

from metadatax_equipment.models import HydrophoneSpecification


@admin.register(HydrophoneSpecification)
class HydrophoneSpecificationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "sensitivity",
        "directivity",
        "operating_min_temperature",
        "operating_max_temperature",
        "min_bandwidth",
        "max_bandwidth",
        "min_dynamic_range",
        "max_dynamic_range",
        "min_operating_depth",
        "max_operating_depth",
        "noise_floor",
    ]
    list_filter = [
        "directivity"
    ]
