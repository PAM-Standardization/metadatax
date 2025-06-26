"""Acquisition metadata administration"""
from django.contrib import admin

from metadatax_data.models import FileFormat


@admin.register(FileFormat)
class FileFormatAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    search_fields = [
        "name",
    ]
