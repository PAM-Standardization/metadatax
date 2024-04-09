"""Acquisition metadata administration"""
from django.contrib import admin

from metadatax.models.data import (
    File,
)


class FileAdmin(admin.ModelAdmin):
    """File presentation in DjangoAdmin"""

    search_fields = [
        "channel_configuration__channel_name",
    ]
    list_filter = [
        "channel_configuration__deployment__project__accessibility",
        "channel_configuration__continuous",
        "format",
        "channel_configuration__hydrophone",
        "channel_configuration__recorder",
    ]


admin.site.register(File, FileAdmin)
