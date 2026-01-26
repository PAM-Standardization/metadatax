"""Acquisition metadata administration"""
import re

from django.contrib import admin, messages
from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django_admin_multiple_choice_list_filter.list_filters import (
    MultipleChoiceListFilter,
)
from django_extension.admin import ExtendedModelAdmin

from metadatax.acquisition.forms import ChannelConfigurationForm
from metadatax.acquisition.models import ChannelConfiguration
from metadatax.acquisition.serializers import ChannelConfigurationSerializer
from metadatax.equipment.models import Equipment


# Source - https://stackoverflow.com/a/4054256
# Posted by Jeff Triplett
# Retrieved 2026-01-09, License - CC BY-SA 2.5


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
class ChannelConfigurationAdmin(ExtendedModelAdmin):
    """ChannelConfiguration presentation in DjangoAdmin"""

    form = ChannelConfigurationForm
    serializer = ChannelConfigurationSerializer
    list_display = [
        "id",
        "deployment",
        "display_recorder_specification",
        "display_detector_specification",
        "list_storages",
        "continuous",
        "duty_cycle_on",
        "duty_cycle_off",
        "instrument_depth",
        "timezone",
        "harvest_starting_date",
        "harvest_ending_date",
        "recording_start_date",
        "recording_end_date",
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
    ]

    fieldsets = [
        (None, {
            'fields': [
                'deployment',
                'storages',
                'continuous',
                'duty_cycle_on',
                'duty_cycle_off',
                'instrument_depth',
                'timezone',
                'harvest_starting_date',
                'harvest_ending_date',
                'extra_information'
            ],
        }),
        (
            "Recording",
            {
                "classes": ("collapse",),
                "fields": [
                    "recorder",
                    "hydrophone",
                    "recording_formats",
                    "sampling_frequency",
                    "sample_depth",
                    "gain",
                    "channel_name",
                ]
            }
        ),
        (
            "Detections",
            {
                "classes": ("collapse",),
                "fields": [
                    "detector",
                    "output_formats",
                    "labels",
                    "min_frequency",
                    "max_frequency",
                    "filter",
                    "configuration",
                ]
            }
        ),
        (
            "Files",
            {
                "fields": [
                    "csv_audio_file",
                ]
            }
        ),
    ]

    @admin.display(description="Recorder specification")
    def display_recorder_specification(self, obj: ChannelConfiguration):
        if not obj.recorder_specification:
            return None
        return mark_safe("<br/>".join(re.split(r"\s-\s", obj.recorder_specification.__str__())))

    @admin.display(description="Detector specification")
    def display_detector_specification(self, obj: ChannelConfiguration):
        if not obj.detector_specification:
            return None
        return mark_safe("<br/>".join(re.split(r"\s-\s", obj.detector_specification.__str__())))

    @admin.display(description="Storages")
    def list_storages(self, obj: ChannelConfiguration):
        return ", ".join([str(e) for e in obj.storages.all()])

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "storages":
            kwargs["queryset"] = Equipment.objects.filter(
                model__specification_relations__specification_type__model="StorageSpecification".lower()
            )
            kwargs[
                "help_text"
            ] = """
                Only storages are shown here.
                If an instrument is missing, update one or add a new one in the Metadatax Equipment > Equipment table.
            """
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    @admin.action(description="Duplicate selected record")
    @transaction.atomic()
    def duplicate_event(self, request, queryset):
        if queryset.count() != 1:
            self.message_user(request, "You should select only one record to duplicate", level=messages.ERROR)
            return
        object: ChannelConfiguration = queryset.first()
        object.id = None
        if object.recorder_specification is not None:
            rs = object.recorder_specification
            recording_formats = rs.recording_formats.all()
            rs.id = None
            rs.save()
            for ff in recording_formats:
                rs.recording_formats.add(ff)
            object.recorder_specification = rs
        if object.detector_specification is not None:
            ds = object.detector_specification
            output_formats = ds.output_formats.all()
            labels = ds.labels.all()
            ds.id = None
            ds.save()
            for ff in output_formats:
                ds.output_formats.add(ff)
            for l in labels:
                ds.labels.add(l)
            object.detector_specification = ds
        object.save()

        return HttpResponseRedirect(
            reverse('admin:acquisition_channelconfiguration_change', kwargs={'object_id': object.id})
        )

    actions = [duplicate_event, "export",]
