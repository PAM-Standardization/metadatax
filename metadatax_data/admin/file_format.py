"""Acquisition metadata administration"""
from django.contrib import admin

from metadatax.models.data import FileFormat


@admin.register(FileFormat)
class FileFormatAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    search_fields = [
        "name",
    ]
