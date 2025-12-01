from django.contrib import admin
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
        "purchase_date",
        "name",
        "sensitivity",
    ]
    search_fields = [
        "serial_number",
        "model__name",
        "owner__name",
        "owner__mail",
        "model__provider__name",
        "model__provider__mail",
        "name",
        "model__specification_relations__specification_type__model",
        "sensitivity",
    ]
    list_filter = [
        "model__specification_relations__specification_type__model",
    ]
    autocomplete_fields = [
        "owner",
    ]
