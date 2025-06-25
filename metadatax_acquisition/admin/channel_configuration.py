"""Acquisition metadata administration"""
import csv
import io
from typing import Optional

from django import forms
from django.contrib import admin
from django.core import validators
from django.core.files.uploadedfile import InMemoryUploadedFile

from metadatax_acquisition.models import ChannelConfiguration
from metadatax_data.models import FileFormat
from utils.admin import JSONExportModelAdmin


class ChannelConfigurationForm(forms.ModelForm):
    csv_file = forms.FileField(
        help_text="Conflicting files will be ignored",
        validators=[validators.FileExtensionValidator(["csv"])],
        required=False,
    )

    class Meta:
        model = ChannelConfiguration
        fields = "__all__"

    def save(self, commit=True):
        instance: ChannelConfiguration = super().save(commit=commit)
        csv_file: Optional[InMemoryUploadedFile] = self.cleaned_data.get(
            "csv_file", None
        )
        if csv_file is None:
            return instance
        content = csv_file.read().decode("utf-8")
        files: list[File] = []
        file: dict
        for file in csv.DictReader(io.StringIO(content)):
            _format, _ = FileFormat.objects.get_or_create(
                name=str(file["format"]).upper()
            )
            files.append(
                File(
                    channel_configuration=instance,
                    name=file["name"],
                    format=_format,
                    initial_timestamp=file["initial_timestamp"],
                    duration=file["duration"],
                    sampling_frequency=file["sampling_frequency"],
                    sample_depth=file["sample_depth"],
                    storage_location=file["storage_location"],
                    file_size=file["file_size"],
                    accessibility=file["accessibility"],
                )
            )

        File.objects.bulk_create(files, ignore_conflicts=True)
        return instance


@admin.register(ChannelConfiguration)
class ChannelConfigurationAdmin(JSONExportModelAdmin):
    """ChannelConfiguration presentation in DjangoAdmin"""

    model = ChannelConfiguration
    form = ChannelConfigurationForm
    serializer = ChannelConfigurationSerializer
    list_display = [
        "id",
        "deployment",
        "recorder_specification",
        "detector_specification",
        "list_other_equipments",
        "continuous",
        "duty_cycle_on",
        "duty_cycle_off",
        "instrument_depth",
        "timezone",
        "harvest_starting_date",
        "harvest_ending_date",
    ]
    search_fields = [
        "deployment__name",
        "deployment__project__name",
        "deployment__campaign__name",
        "deployment__site__name",
    ]
    list_filter = [
        "deployment__project__accessibility",
        "continuous",
    ]

    @admin.display(description="Other equipments")
    def list_other_equipments(self, obj: ChannelConfiguration):
        return ", ".join([str(e) for e in obj.other_equipments.all()])
