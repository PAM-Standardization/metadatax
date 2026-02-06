from django.contrib import admin
from django.db.models import Exists, OuterRef, Q
from django.utils.translation import gettext_lazy as _
from django_admin_multiple_choice_list_filter.list_filters import (
    MultipleChoiceListFilter,
)
from django_extension.admin import ExtendedModelAdmin

from metadatax.equipment.forms.equipment import EquipmentForm
from metadatax.equipment.models import Equipment, StorageSpecification, RecorderSpecification, HydrophoneSpecification, \
    AcousticDetectorSpecification, EquipmentModelSpecification
from metadatax.equipment.serializers import EquipmentSerializer


class EquipmentTypeFilter(MultipleChoiceListFilter):
    title = _("Type")
    parameter_name = "type__in"

    def lookups(self, request, model_admin):
        return [
            (StorageSpecification.__name__.lower(), "Storage"),
            (RecorderSpecification.__name__.lower(), "Recorder"),
            (HydrophoneSpecification.__name__.lower(), "Hydrophone"),
            (AcousticDetectorSpecification.__name__.lower(), "Acoustic detector"),
        ]

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        filters = Q()
        for model in self.value_as_list():
            filters = filters & Exists(
                EquipmentModelSpecification.objects.filter(
                    model_id=OuterRef('model_id'),
                    specification_type__model=model
                )
            )
        return queryset.filter(filters)


@admin.register(Equipment)
class EquipmentAdmin(ExtendedModelAdmin):
    actions = ["export", ]
    serializer = EquipmentSerializer
    form = EquipmentForm
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
        "model__provider__name",
        "model__provider__mail",
        "name",
        "model__specification_relations__specification_type__model",
        "sensitivity",
    ]
    list_filter = [
        EquipmentTypeFilter,
    ]

    fieldsets = [
        (
            None, {"fields": [
            "model",
            "serial_number",
            "owner",
            "purchase_date",
            "name",
            "sensitivity",
        ]}
        )
    ]

    @admin.display()
    def owner(self, equipment: Equipment):
        return f"{equipment.owner.__class__.__name__}: {equipment.owner}"
