from django.contrib import admin

from metadatax.equipment.models import MaintenanceType


@admin.register(MaintenanceType)
class MaintenanceTypeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "_interval",
    ]
    search_fields = [
        "name",
    ]
