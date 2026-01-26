from django.contrib import admin
from django_extension.admin import ExtendedModelAdmin

from metadatax.equipment.forms.platform import PlatformForm
from metadatax.equipment.models import Platform
from metadatax.equipment.serializers.platform import PlatformSerializer


@admin.register(Platform)
class PlatformAdmin(ExtendedModelAdmin):
    actions = ["export",]
    serializer = PlatformSerializer
    form = PlatformForm
    list_display = [
        "name",
        "type",
        "owner",
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

    @admin.display()
    def owner(self, platform: Platform):
        if platform.owner is None:
            return self.get_empty_value_display()
        return f"{platform.owner.__class__.__name__}: {platform.owner}"
