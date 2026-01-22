from django.contrib import admin
from django_extension.admin import ExtendedModelAdmin

from metadatax.equipment.models import MaintenanceType


@admin.register(MaintenanceType)
class MaintenanceTypeAdmin(ExtendedModelAdmin):
    hidden = True

    list_display = [
        "name",
        "description",
        "_interval",
    ]
    search_fields = [
        "name",
    ]
