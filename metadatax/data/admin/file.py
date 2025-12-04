from django import forms
from django.contrib import admin
from django.forms import widgets

from metadatax.common.models.enums import Accessibility
from metadatax.data.models import File


class FileForm(forms.ModelForm):
    accessibility = forms.CharField(
        widget=widgets.RadioSelect(choices=Accessibility.choices)
    )

    class Meta:
        model = File
        fields = "__all__"


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    form = FileForm
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
    autocomplete_fields = [
        "format",
    ]
