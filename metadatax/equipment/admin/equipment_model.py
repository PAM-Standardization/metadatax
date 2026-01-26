from django.contrib import admin
from django.db.models import Q, Exists, OuterRef
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django_admin_multiple_choice_list_filter.list_filters import MultipleChoiceListFilter
from django_extension.admin import ExtendedModelAdmin

from metadatax.equipment.forms.equipment_model import EquipmentModelForm
from metadatax.equipment.models import EquipmentModel, AcousticDetectorSpecification, HydrophoneSpecification, \
    RecorderSpecification, StorageSpecification, HydrophoneDirectivity, EquipmentModelSpecification
from metadatax.equipment.serializers import EquipmentModelSerializer


class SpecificationTypeFilter(MultipleChoiceListFilter):
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
            filters  = filters & Exists(
                EquipmentModelSpecification.objects.filter(
                    model_id=OuterRef('pk'),
                    specification_type__model=model
                )
            )
        return queryset.filter(filters)


@admin.register(EquipmentModel)
class EquipmentModelAdmin(ExtendedModelAdmin):
    actions = ["export",]
    serializer = EquipmentModelSerializer
    form = EquipmentModelForm
    list_display = [
        "name",
        "provider",
        "battery_slots_count",
        "battery_type",
        "cables",
        "storage",
        "recorder",
        "hydrophone",
        "acoustic_detector"
    ]
    search_fields = [
        "name",
        "provider__name",
        "provider__mail",
        "specification_relations__specification_type__model",
    ]
    list_filter = [
        SpecificationTypeFilter,
    ]
    autocomplete_fields = [
        "provider",
    ]

    fieldsets = [
        (
            None,
            {
                "fields": [
                    "name",
                    "provider",
                    "battery_slots_count",
                    "battery_type",
                    "cables",
                ]
            },
        ),
        (
            "Internal Storage",
            {
                "classes": ("collapse",),
                "fields": [
                    "capacity",
                    "type"
                ]
            }
        ),
        (
            "Recorder",
            {
                "classes": ("collapse",),
                "fields": [
                    "channels_count",
                    "storage_slots_count",
                    "storage_maximum_capacity",
                    "storage_type"
                ]
            }
        ),
        (
            "Hydrophone",
            {
                "classes": ("collapse",),
                "fields": [
                    "directivity",
                    "operating_min_temperature",
                    "operating_max_temperature",
                    "min_bandwidth",
                    "max_bandwidth",
                    "min_dynamic_range",
                    "max_dynamic_range",
                    "min_operating_depth",
                    "max_operating_depth",
                    "noise_floor",
                ]
            }
        ),
        (
            "Acoustic Detector",
            {
                "classes": ("collapse",),
                "fields": [
                    "detected_labels",
                    "min_frequency",
                    "max_frequency",
                    "algorithm_name"
                ]
            }
        )
    ]

    @admin.display(description="Internal Storage")
    def storage(self, obj: EquipmentModel) -> str:
        """Display readable information about storage spec"""
        rels = obj.specification_relations.all()
        if not rels.filter(specification_type__model=StorageSpecification.__name__.lower()).exists():
            return self.get_empty_value_display()
        spec: StorageSpecification = rels.get(
            specification_type__model=StorageSpecification.__name__.lower()).specification

        info  = []
        if spec.capacity is not None:
            info.append(f"Capacity: {spec.capacity}")
        if spec.type is not None:
            info.append(f"Type: {spec.type}")

        if len(info) > 0:
            return mark_safe("<br/>".join(info))
        return mark_safe("<i>No information</i>")

    @admin.display(description="Recorder")
    def recorder(self, obj: EquipmentModel) -> str:
        """Display readable information about recorder spec"""
        rels = obj.specification_relations.all()
        if not rels.filter(specification_type__model=RecorderSpecification.__name__.lower()).exists():
            return self.get_empty_value_display()
        spec: RecorderSpecification = rels.get(
            specification_type__model=RecorderSpecification.__name__.lower()
        ).specification

        info  = []
        if spec.channels_count is not None:
            info.append(f"Channels: {spec.channels_count}")

        storage_info = []
        if spec.storage_slots_count is not None:
            storage_info.append(f"{spec.storage_slots_count} slots")
        if spec.storage_maximum_capacity != None:
            storage_info.append(f"max {spec.storage_maximum_capacity}")
        if spec.storage_type is not None:
            storage_info.append(f"{spec.storage_type}")
        if len(storage_info) > 0:
            info.append(f"Storage: {" - ".join(storage_info)}")

        if len(info) > 0:
            return mark_safe("<br/>".join(info))
        return mark_safe("<i>No information</i>")

    @admin.display(description="Hydrophone")
    def hydrophone(self, obj: EquipmentModel) -> str:
        """Display readable information about hydrophone spec"""
        rels = obj.specification_relations.all()
        if not rels.filter(specification_type__model=HydrophoneSpecification.__name__.lower()).exists():
            return self.get_empty_value_display()
        spec: HydrophoneSpecification = rels.get(
            specification_type__model=HydrophoneSpecification.__name__.lower()
        ).specification

        info  = []
        if spec.directivity is not None:
            info.append(HydrophoneDirectivity(spec.directivity).label)

        if spec.min_bandwidth is not None or spec.max_bandwidth is not None:
            info.append(f"Bandwidth: {spec.min_bandwidth}<{spec.max_bandwidth} Hz")

        if spec.min_dynamic_range is not None or spec.max_dynamic_range is not None:
            info.append(f"Dynamic range: {spec.min_dynamic_range}<{spec.max_dynamic_range} dB SPL RMS or peak")

        if spec.operating_min_temperature is not None or spec.operating_max_temperature is not None:
            info.append(f"Operating T°: {spec.operating_min_temperature}<{spec.operating_max_temperature} °C")

        if spec.min_operating_depth is not None or spec.max_operating_depth is not None:
            info.append(f"Operating Depth: {spec.min_operating_depth}<{spec.max_operating_depth} m")

        if spec.noise_floor is not None:
            info.append(f"Noise floor: {spec.noise_floor}dB re 1µPa^2/Hz")

        if len(info) > 0:
            return mark_safe("<br/>".join(info))
        return mark_safe("<i>No information</i>")

    @admin.display(description="Acoustic Detector")
    def acoustic_detector(self, obj: EquipmentModel) -> str:
        """Display readable information about acoustic detector spec"""
        rels = obj.specification_relations.all()
        if not rels.filter(specification_type__model=AcousticDetectorSpecification.__name__.lower()).exists():
            return self.get_empty_value_display()
        spec: AcousticDetectorSpecification = rels.get(
            specification_type__model=AcousticDetectorSpecification.__name__.lower()).specification

        info  = []
        if spec.detected_labels.count() > 0:
            info.append("Labels: " + ", ".join([str(label) for label in spec.detected_labels.all()]))

        if spec.min_frequency is not None or spec.max_frequency is not None:
            info.append(f"Frequency: [{spec.min_frequency}; {spec.max_frequency}]Hz")
        if spec.algorithm_name is not None:
            info.append(f"Algorithm: {spec.algorithm_name}")

        if len(info) > 0:
            return mark_safe("<br/>".join(info))
        return mark_safe("<i>No information</i>")
