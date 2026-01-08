from django.contrib import admin
from django_extended.admin import HiddenModelAdmin

from metadatax.equipment.models import PlatformType


@admin.register(PlatformType)
class PlatformTypeAdmin(HiddenModelAdmin):
    model = PlatformType
    list_display = ["name", "is_mobile"]
    search_fields = [
        "name",
    ]
    list_filter = [
        "is_mobile",
    ]
