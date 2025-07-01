from django.contrib import admin

from metadatax.equipment.models import Platform
from metadatax.equipment.serializers.platform import PlatformSerializer
from metadatax.utils import JSONExportModelAdmin


@admin.register(Platform)
class PlatformAdmin(JSONExportModelAdmin):
    model = Platform
    serializer = PlatformSerializer
    list_display = [
        "type",
        "owner",
        "provider",
        "name",
        "description",
    ]
    search_fields = [
        "name",
        "type__name",
        "owner__name",
        "owner__mail",
        "provider__name",
        "provider__mail",
    ]
    list_filter = ["type"]
