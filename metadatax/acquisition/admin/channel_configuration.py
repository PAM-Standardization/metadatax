"""Acquisition metadata administration"""

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django_admin_multiple_choice_list_filter.list_filters import (
    MultipleChoiceListFilter,
)
from django_extended.admin import JSONExportModelAdmin

from metadatax.acquisition.forms import ChannelConfigurationForm
from metadatax.acquisition.models import ChannelConfiguration
from metadatax.acquisition.serializers import ChannelConfigurationSerializer
from metadatax.equipment.models import Equipment


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

    @admin.display(description="Storages")
    def list_storages(self, obj: ChannelConfiguration):
        return ", ".join([str(e) for e in obj.storages.all()])

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "storages":
            kwargs["queryset"] = Equipment.objects.filter(
                model__specification_relations__specification_type__model="StorageSpecification"
            )
            kwargs[
                "help_text"
            ] = """
                Only storages are shown here.
                If an instrument is missing, update one or add a new one in the Metadatax Equipment > Equipment table.
            """
        return super().formfield_for_manytomany(db_field, request, **kwargs)
