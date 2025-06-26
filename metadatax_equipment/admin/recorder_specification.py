from django.contrib import admin

from metadatax_equipment.models import RecorderSpecification


@admin.register(RecorderSpecification)
class RecorderSpecificationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "channels_count",
        "sd_slots_count",
        "sd_maximum_capacity",
        "sd_type",
    ]
    search_fields = [
        "sd_type"
    ]
