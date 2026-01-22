from django.contrib import admin
from django.utils.safestring import mark_safe
from django_extension.admin import ExtendedModelAdmin

from metadatax.equipment.forms.equipment_model import EquipmentModelForm
from metadatax.equipment.models import EquipmentModel, AcousticDetectorSpecification, HydrophoneSpecification, \
    RecorderSpecification, StorageSpecification
from metadatax.equipment.serializers import EquipmentModelSerializer


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
        "specification_relations__specification_type__model",
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
        if rels.filter(specification_type__model=StorageSpecification.__name__.lower()).exists():
            spec: StorageSpecification = rels.get(
                specification_type__model=StorageSpecification.__name__.lower()).specification
            return mark_safe("<br/>".join([
                f"Capacity: {spec.capacity}",
                f"Type: {spec.type}",
            ]))

    @admin.display(description="Recorder")
    def recorder(self, obj: EquipmentModel) -> str:
        """Display readable information about recorder spec"""
        rels = obj.specification_relations.all()
        if rels.filter(specification_type__model=RecorderSpecification.__name__.lower()).exists():
            spec: RecorderSpecification = rels.get(
                specification_type__model=RecorderSpecification.__name__.lower()).specification
            return mark_safe("<br/>".join([
                f"Channels: {spec.channels_count}",
                f"Storage: {spec.storage_slots_count} - {spec.storage_maximum_capacity} - {spec.storage_type}",
            ]))

    @admin.display(description="Hydrophone")
    def hydrophone(self, obj: EquipmentModel) -> str:
        """Display readable information about hydrophone spec"""
        rels = obj.specification_relations.all()
        if rels.filter(specification_type__model=HydrophoneSpecification.__name__.lower()).exists():
            spec: HydrophoneSpecification = rels.get(
                specification_type__model=HydrophoneSpecification.__name__.lower()).specification
            return mark_safe("<br/>".join([
                spec.directivity,
                f"Bandwidth: [{spec.min_bandwidth}; {spec.max_bandwidth}]Hz",
                f"Dynamic range: [{spec.min_dynamic_range}; {spec.max_dynamic_range}] dB SPL RMS or peak",
                f"Operating T°: [{spec.operating_min_temperature}; {spec.operating_max_temperature}]°C",
                f"Operating Depth: [{spec.min_operating_depth}; {spec.max_operating_depth}]m",
                f"Noise floor: [{spec.noise_floor}dB re 1µPa^2/Hz",
            ]))

    @admin.display(description="Acoustic Detector")
    def acoustic_detector(self, obj: EquipmentModel) -> str:
        """Display readable information about acoustic detector spec"""
        rels = obj.specification_relations.all()
        if rels.filter(specification_type__model=AcousticDetectorSpecification.__name__.lower()).exists():
            spec: AcousticDetectorSpecification = rels.get(
                specification_type__model=AcousticDetectorSpecification.__name__.lower()).specification
            return mark_safe("<br/>".join([
                "Labels: " + ", ".join([str(label) for label in spec.detected_labels.all()]),
                f"Frequency: [{spec.min_frequency}; {spec.max_frequency}]Hz",
                f"Algorithm: {spec.algorithm_name}"
            ]))
