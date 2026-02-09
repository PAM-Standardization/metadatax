from typing import Optional, Callable
from django import forms
from django.db import  models
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model, QuerySet
from django.utils.safestring import mark_safe
from rest_framework.reverse import reverse
from django.utils.html import format_html

from metadatax.equipment.forms.equipment_model import EquipmentModelForm
from metadatax.equipment.models import EquipmentModel, AcousticDetectorSpecification, HydrophoneSpecification, \
    RecorderSpecification, StorageSpecification, EquipmentModelSpecification
from metadatax.equipment.serializers import EquipmentModelSerializer
from metadatax.utils import JSONExportModelAdmin


class AbstractSpecificationAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        '__str__',
        'usage'
    ]
    readonly_fields = (
        'usage',
    )

    class Meta:
        abstract = True

    @staticmethod
    def _get_edit_link(obj: Model, to_str: Callable[[Model], str] = lambda x: str(x)):
        app = obj._meta.app_label
        model = obj._meta.model_name
        view = f"admin:{app}_{model}_change"
        link = reverse(view, args=[obj.pk])
        return format_html('<a href="{}">{}</a>', link, to_str(obj))

    @admin.display(description="Usages")
    def usage(self, obj) -> Optional[str]:
        rels = EquipmentModelSpecification.objects.filter(
            specification_type__model=self.model.__name__.lower(),
            specification_id=obj.id
        )
        if not rels.exists():
            return None
        return mark_safe("<br/>".join([
            self._get_edit_link(rel)
            for rel in rels
        ]))



@admin.register(EquipmentModelSpecification)
class EquipmentModelSpecificationModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'model',
        'specification'
    ]
    readonly_fields = (
        'specification',
    )
    list_filter = [
        "model",
    ]


@admin.register(RecorderSpecification)
class RecorderSpecificationModelAdmin(AbstractSpecificationAdmin):
    pass


@admin.register(StorageSpecification)
class StorageSpecificationModelAdmin(AbstractSpecificationAdmin):
    pass


@admin.register(HydrophoneSpecification)
class HydrophoneSpecificationModelAdmin(AbstractSpecificationAdmin):
    pass


@admin.register(AcousticDetectorSpecification)
class AcousticDetectorSpecificationModelAdmin(AbstractSpecificationAdmin):
    pass


@admin.register(EquipmentModel)
class EquipmentModelAdmin(JSONExportModelAdmin):
    model = EquipmentModel
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
                "fields": [
                    "capacity",
                    "type"
                ]
            }
        ),
        (
            "Recorder",
            {
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
                "fields": [
                    "detected_labels",
                    "min_frequency",
                    "max_frequency",
                    "algorithm_name"
                ]
            }
        )
    ]

    @staticmethod
    def _get_edit_link(obj: Model, to_str: Callable[[Model], str] = lambda x: str(x)):
        app = obj._meta.app_label
        model = obj._meta.model_name
        view = f"admin:{app}_{model}_change"
        link = reverse(view, args=[obj.pk])
        return format_html('<a href="{}">{}</a>', link, to_str(obj))

    @admin.display(description="Internal Storage")
    def storage(self, obj: EquipmentModel) -> Optional[str]:
        """Display readable information about storage spec"""
        rels = obj.specification_relations.filter(specification_type__model=StorageSpecification.__name__.lower())
        if not rels.exists():
            return self.get_empty_value_display()
        infos = []
        for rel in rels:
            spec = rel.specification
            infos.append("<br/>".join([
                self._get_edit_link(spec),
                f"Capacity: {spec.capacity}",
                f"Type: {spec.type}",
            ]))
        return mark_safe("<br/>--<br/>".join(infos))

    @admin.display(description="Recorder")
    def recorder(self, obj: EquipmentModel) -> Optional[str]:
        """Display readable information about recorder spec"""
        rels = obj.specification_relations.filter(specification_type__model=RecorderSpecification.__name__.lower())
        if not rels.exists():
            return self.get_empty_value_display()
        infos = []
        for rel in rels:
            spec = rel.specification
            infos.append("<br/>".join([
                self._get_edit_link(spec),
                f"Channels: {spec.channels_count}",
                f"Storage: {spec.storage_slots_count} - {spec.storage_maximum_capacity} - {spec.storage_type}",
            ]))
        return mark_safe("<br/>--<br/>".join(infos))

    @admin.display(description="Hydrophone")
    def hydrophone(self, obj: EquipmentModel) -> Optional[str]:
        """Display readable information about hydrophone spec"""
        rels = obj.specification_relations.filter(specification_type__model=HydrophoneSpecification.__name__.lower())
        if not rels.exists():
            return self.get_empty_value_display()
        infos = []
        for rel in rels:
            spec = rel.specification
            infos.append("<br/>".join([
                self._get_edit_link(spec),
                spec.directivity or 'None',
                f"Bandwidth: [{spec.min_bandwidth}; {spec.max_bandwidth}]Hz",
                f"Dynamic range: [{spec.min_dynamic_range}; {spec.max_dynamic_range}] dB SPL RMS or peak",
                f"Operating T°: [{spec.operating_min_temperature}; {spec.operating_max_temperature}]°C",
                f"Operating Depth: [{spec.min_operating_depth}; {spec.max_operating_depth}]m",
                f"Noise floor: [{spec.noise_floor}dB re 1µPa^2/Hz",
            ]))
        return mark_safe("<br/>--<br/>".join(infos))

    @admin.display(description="Acoustic Detector")
    def acoustic_detector(self, obj: EquipmentModel) -> Optional[str]:
        """Display readable information about acoustic detector spec"""
        rels = obj.specification_relations.filter(
            specification_type__model=AcousticDetectorSpecification.__name__.lower())
        if not rels.exists():
            return self.get_empty_value_display()
        infos = []
        for rel in rels:
            spec = rel.specification
            infos.append("<br/>".join([
                self._get_edit_link(spec),
                "Labels: " + ", ".join([str(label) for label in spec.detected_labels.all()]),
                f"Frequency: [{spec.min_frequency}; {spec.max_frequency}]Hz",
                f"Algorithm: {spec.algorithm_name}"
            ]))
        return mark_safe("<br/>--<br/>".join(infos))
