from django.contrib import admin
from django.contrib.admin import EmptyFieldListFilter
from django.utils.translation import gettext_lazy as _
from django_admin_multiple_choice_list_filter.list_filters import (
    MultipleChoiceListFilter,
)

from metadatax.equipment.models import Equipment
from metadatax.equipment.serializers import EquipmentSerializer
from metadatax.utils import JSONExportModelAdmin


class EquipmentTypeFilter(MultipleChoiceListFilter):
    title = _("Type")
    parameter_name = "type__in"

    def lookups(self, request, model_admin):
        return [
            ("storage_specification", "Storage"),
            ("recorder_specification", "Recorder"),
            ("hydrophone_specification", "Hydrophone"),
            ("acoustic_detector_specification", "Acoustic detector"),
        ]

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        filters = {}
        for filter in self.value_as_list():
            filters[filter + "__isnull"] = False
        return queryset.filter(**filters)


@admin.register(Equipment)
class EquipmentAdmin(JSONExportModelAdmin):
    model = Equipment
    serializer = EquipmentSerializer
    list_display = [
        "serial_number",
        "model",
        "owner",
        "provider",
        "storage_specification",
        "recorder_specification",
        "hydrophone_specification",
        "acoustic_detector_specification",
        "purchase_date",
        "name",
        "battery_slots_count",
        "battery_type",
        "cables",
    ]
    search_fields = [
        "serial_number",
        "model",
        "owner__name",
        "owner__mail",
        "provider__name",
        "provider__mail",
        "name",
        "acoustic_detector_specification__detected_labels__nickname",
        "acoustic_detector_specification__detected_labels__source__english_name",
        "acoustic_detector_specification__detected_labels__sound__english_name",
        "acoustic_detector_specification__algorithm_name",
    ]
    list_filter = [
        ("recorder_specification", EmptyFieldListFilter),
        EquipmentTypeFilter,
        "hydrophone_specification__directivity",
    ]
    autocomplete_fields = [
        "owner",
        "provider",
        "storage_specification",
        "recorder_specification",
        "hydrophone_specification",
        "acoustic_detector_specification",
    ]

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, request, **kwargs)
        if (
            db_field.name == "storage_specification"
            or db_field.name == "recorder_specification"
            or db_field.name == "hydrophone_specification"
            or db_field.name == "acoustic_detector_specification"
        ):
            formfield.widget.can_delete_related = False
            formfield.widget.can_change_related = False
        return formfield
