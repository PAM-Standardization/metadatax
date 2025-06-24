from django.contrib import admin

from metadatax_equipment.models import PlatformType


@admin.register(PlatformType)
class PlatformTypeAdmin(admin.ModelAdmin):
    model = PlatformType
    list_display = [
        "name",
        "is_mobile"
    ]
    search_fields = [
        "name",
    ]
    list_filter = [
        "is_mobile",
    ]
