from django.contrib import admin

from metadatax.equipment.models import Maintenance


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = [
        "type",
        "date",
        "platform",
        "equipment",
        "description",
        "maintainer",
        "maintainer_institution",
    ]
    search_fields = [
        "type__name",
        "platform__type__name",
        "platform__name",
        "equipment__serial_number",
        "equipment__model",
        "equipment__name",
        "maintainer__first_name",
        "maintainer__last_name",
        "maintainer__mail",
        "maintainer_institution__name",
        "maintainer_institution__mail",
    ]
    autocomplete_fields = [
        "type",
        "maintainer",
        "maintainer_institution",
        "platform",
        "equipment",
    ]
