from django.contrib import admin
from django_extended.admin import JSONExportModelAdmin

from metadatax.equipment.forms.platform import PlatformForm
from metadatax.equipment.models import Platform
from metadatax.equipment.serializers.platform import PlatformSerializer


@admin.register(Platform)
class PlatformAdmin(JSONExportModelAdmin):
    model = Platform
    serializer = PlatformSerializer
    form = PlatformForm
    list_display = [
        "name",
        "type",
        # "owner", TODO
        "provider",
        "description",
    ]
    search_fields = [
        "name",
        "type__name",
        "provider__name",
        "provider__mail",
    ]
    list_filter = [
        "type",
    ]
    autocomplete_fields = [
        "type",
        "provider",
    ]
    fieldsets = [
        (None, {
            'fields': [
                "owner",
                "provider",
                "type",
                "name",
                "description",
            ],
        }),
    ]
