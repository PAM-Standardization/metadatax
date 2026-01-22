from django.contrib import admin
from django_extension.admin import ExtendedModelAdmin

from metadatax.equipment.models import PlatformType


@admin.register(PlatformType)
class PlatformTypeAdmin(ExtendedModelAdmin):
    hidden = True

    list_display = ["name", "is_mobile"]
    search_fields = [
        "name",
    ]
    list_filter = [
        "is_mobile",
    ]
