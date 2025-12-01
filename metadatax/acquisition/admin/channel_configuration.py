"""Acquisition metadata administration"""
import csv
import io
from typing import Optional

from django import forms
from django.contrib import admin
from django.core import validators
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.translation import gettext_lazy as _
from django_admin_multiple_choice_list_filter.list_filters import (
    MultipleChoiceListFilter,
)

from metadatax.acquisition.models import ChannelConfiguration
from metadatax.acquisition.serializers import ChannelConfigurationSerializer
from metadatax.data.models import FileFormat, File, AudioProperties
from metadatax.equipment.models import Equipment
from metadatax.utils import JSONExportModelAdmin


class ChannelConfigurationForm(forms.ModelForm):
    csv_audio_file = forms.FileField(
        help_text="Conflicting files will be ignored. "
                  "The file should contains the following columns: "
                  "name* (file name),  "
                  "format* (file format)," 
                  "initial_timestamp*, "
                  "duration*, "
                  "sampling_frequency*, "
                  "storage_location, "
                  "file_size, "
                  "accessibility (C - Confidential, R - upon Request, O - Open), "
                  "sample_depth, "
        ,
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
        audio_properties: list[AudioProperties] = []
        files: list[File] = []
        file: dict
        for file in csv.DictReader(io.StringIO(content)):
            _format, _ = FileFormat.objects.get_or_create(
                name=str(file["format"]).upper()
            )
            audio = AudioProperties(
                sampling_frequency=file["sampling_frequency"],
                initial_timestamp=file["initial_timestamp"],
                duration=file["duration"],
                sample_depth=file["sample_depth"],
            )
            audio_properties.append(audio)
            files.append(
                File(
                    filename=file["name"],
                    format=_format,
                    audio_properties=audio,
                    storage_location=file["storage_location"],
                    file_size=file["file_size"],
                    accessibility=file["accessibility"],
                )
            )

        AudioProperties.objects.bulk_create(audio_properties, ignore_conflicts=True)
        instance.files.bulk_create(files, ignore_conflicts=True)
        return instance


class ChannelConfigurationTypeFilter(MultipleChoiceListFilter):
    title = _("Type")
    parameter_name = "type__in"

    def lookups(self, request, model_admin):
        return [
            ("recorder_specification", "Recorder"),
            ("detector_specification", "Acoustic detector"),
        ]

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        filters = {}
        for filter in self.value_as_list():
            filters[filter + "__isnull"] = False
        return queryset.filter(**filters)


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
        "list_storages",
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
        ChannelConfigurationTypeFilter,
        "deployment__project__accessibility",
        "continuous",
    ]
    filter_horizontal = [
        "storages",
    ]
    autocomplete_fields = [
        "deployment",
        "recorder_specification",
    ]

    @admin.display(description="Storages")
    def list_storages(self, obj: ChannelConfiguration):
        return ", ".join([str(e) for e in obj.storages.all()])

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "storages":
            kwargs["queryset"] = Equipment.objects.filter(
                storage_specification__isnull=False
            )
            kwargs[
                "help_text"
            ] = """
                Only storages are shown here.
                If an instrument is missing, update one or add a new one in the Metadatax Equipment > Equipment table.
            """
        return super().formfield_for_manytomany(db_field, request, **kwargs)
