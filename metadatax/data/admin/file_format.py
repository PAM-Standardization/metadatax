"""Acquisition metadata administration"""
from django.contrib import admin
from django_extension.admin import ExtendedModelAdmin

from metadatax.data.models import FileFormat


@admin.register(FileFormat)
class FileFormatAdmin(ExtendedModelAdmin):
    list_display = [
        "name",
    ]
    search_fields = [
        "name",
    ]
