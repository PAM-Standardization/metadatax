from django.contrib import admin

from metadatax.data.models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = [
        "filename",
        "format",
        "audio_properties",
        "detection_properties",
        "storage_location",
        "file_size",
        "accessibility",
    ]
    search_fields = [
        "filename",
        "storage_location",
    ]
    list_filter = [
        "format",
        "accessibility",
    ]
