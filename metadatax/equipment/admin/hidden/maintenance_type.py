from django.contrib import admin
from django_extended.admin import HiddenModelAdmin

from metadatax.equipment.models import MaintenanceType


@admin.register(MaintenanceType)
class MaintenanceTypeAdmin(HiddenModelAdmin):
    list_display = [
        "name",
        "description",
        "_interval",
    ]
    search_fields = [
        "name",
    ]
