from django.contrib import admin

from metadatax.equipment.models import RecorderSpecification


@admin.register(RecorderSpecification)
class RecorderSpecificationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "channels_count",
        "storage_slots_count",
        "storage_maximum_capacity",
        "storage_type",
    ]
    search_fields = [
        "channels_count",
        "storage_slots_count",
        "storage_maximum_capacity",
        "storage_type",
    ]
