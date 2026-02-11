from typing import Optional

from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from django.db.models import QuerySet, Q
from django_extension.forms.widgets import AdminAutocompleteSelectMultipleWidget

from metadatax.equipment.models import EquipmentModel, StorageSpecification, RecorderSpecification, \
    EquipmentModelSpecification, HydrophoneSpecification, AcousticDetectorSpecification


class EquipmentModelForm(forms.ModelForm):
    # Additional typing
    instance: Optional[EquipmentModel]

    class Meta:
        model = EquipmentModel
        fields = "__all__"

    # Storage
    capacity = StorageSpecification._meta.get_field("capacity").formfield()
    type = StorageSpecification._meta.get_field("type").formfield()

    # Recorder
    channels_count = RecorderSpecification._meta.get_field("channels_count").formfield()
    storage_slots_count = RecorderSpecification._meta.get_field("storage_slots_count").formfield()
    storage_maximum_capacity = RecorderSpecification._meta.get_field("storage_maximum_capacity").formfield()
    storage_type = RecorderSpecification._meta.get_field("storage_type").formfield()

    # Hydrophone
    directivity = HydrophoneSpecification._meta.get_field("directivity").formfield()
    operating_min_temperature = HydrophoneSpecification._meta.get_field("operating_min_temperature").formfield()
    operating_max_temperature = HydrophoneSpecification._meta.get_field("operating_max_temperature").formfield()
    min_bandwidth = HydrophoneSpecification._meta.get_field("min_bandwidth").formfield()
    max_bandwidth = HydrophoneSpecification._meta.get_field("max_bandwidth").formfield()
    min_dynamic_range = HydrophoneSpecification._meta.get_field("min_dynamic_range").formfield()
    max_dynamic_range = HydrophoneSpecification._meta.get_field("max_dynamic_range").formfield()
    min_operating_depth = HydrophoneSpecification._meta.get_field("min_operating_depth").formfield()
    max_operating_depth = HydrophoneSpecification._meta.get_field("max_operating_depth").formfield()
    noise_floor = HydrophoneSpecification._meta.get_field("noise_floor").formfield()

    # Acoustic Detector
    detected_labels = AcousticDetectorSpecification._meta.get_field("detected_labels").formfield(
        required=False,
        widget=RelatedFieldWidgetWrapper(
            widget=AdminAutocompleteSelectMultipleWidget(),
            rel=AcousticDetectorSpecification._meta.get_field("detected_labels").remote_field,
            admin_site=admin.site,
            can_add_related=True,
        )
    )
    min_frequency = AcousticDetectorSpecification._meta.get_field("min_frequency").formfield()
    max_frequency = AcousticDetectorSpecification._meta.get_field("max_frequency").formfield()
    algorithm_name = AcousticDetectorSpecification._meta.get_field("algorithm_name").formfield()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance is None:
            pass

        rels = self.instance.specification_relations.all()

        if rels.filter(specification_type__model=StorageSpecification.__name__.lower()).exists():
            spec: StorageSpecification = rels.get(
                specification_type__model=StorageSpecification.__name__.lower()).specification
            self.fields['capacity'].initial = spec.capacity
            self.fields['type'].initial = spec.type

        if rels.filter(specification_type__model=RecorderSpecification.__name__.lower()).exists():
            spec: RecorderSpecification = rels.get(
                specification_type__model=RecorderSpecification.__name__.lower()).specification
            self.fields['channels_count'].initial = spec.channels_count
            self.fields['storage_slots_count'].initial = spec.storage_slots_count
            self.fields['storage_maximum_capacity'].initial = spec.storage_maximum_capacity
            self.fields['storage_type'].initial = spec.storage_type

        if rels.filter(specification_type__model=HydrophoneSpecification.__name__.lower()).exists():
            spec: HydrophoneSpecification = rels.get(
                specification_type__model=HydrophoneSpecification.__name__.lower()).specification
            self.fields['directivity'].initial = spec.directivity
            self.fields['operating_min_temperature'].initial = spec.operating_min_temperature
            self.fields['operating_max_temperature'].initial = spec.operating_max_temperature
            self.fields['min_bandwidth'].initial = spec.min_bandwidth
            self.fields['max_bandwidth'].initial = spec.max_bandwidth
            self.fields['min_dynamic_range'].initial = spec.min_dynamic_range
            self.fields['max_dynamic_range'].initial = spec.max_dynamic_range
            self.fields['min_operating_depth'].initial = spec.min_operating_depth
            self.fields['max_operating_depth'].initial = spec.max_operating_depth
            self.fields['noise_floor'].initial = spec.noise_floor

        if rels.filter(specification_type__model=AcousticDetectorSpecification.__name__.lower()).exists():
            spec: AcousticDetectorSpecification = rels.get(
                specification_type__model=AcousticDetectorSpecification.__name__.lower()).specification
            self.fields['detected_labels'].initial = spec.detected_labels.all()
            self.fields['min_frequency'].initial = spec.min_frequency
            self.fields['max_frequency'].initial = spec.max_frequency
            self.fields['algorithm_name'].initial = spec.algorithm_name

    def save(self, commit=True):
        super().save(commit)

        self.save_model(StorageSpecification)
        self.save_model(RecorderSpecification)
        self.save_model(HydrophoneSpecification)
        self.save_model(AcousticDetectorSpecification)

        return self.instance

    @transaction.atomic
    def save_model(self, model: type, commit=True):
        should_exists = False
        models_fields = {}
        for field in self.cleaned_data:
            if field not in model.__dict__:
                continue
            if self.cleaned_data.get(field) is None:
                continue
            data = self.cleaned_data.get(field)
            if isinstance(data, QuerySet) and not data.exists():
                continue
                should_exists = True
                models_fields[field] = self.cleaned_data.get(field)

        rel: QuerySet[EquipmentModelSpecification] = self.instance.specification_relations.filter(
            specification_type__model=model.__name__.lower())
        spec = rel.first() if rel.exists() else None
        other_rels = EquipmentModelSpecification.objects.filter(
            specification_type__model=model.__name__.lower(),
            specification_id=spec.id if spec else None
        ).filter(~Q(model_id=self.instance.id))

        def create():
            if model == AcousticDetectorSpecification:
                detected_labels = models_fields.pop('detected_labels')
                specification: AcousticDetectorSpecification = model.objects.create(**models_fields)
                for label in detected_labels:
                    specification.detected_labels.add(label)
            else:
                specification = model.objects.create(**models_fields)
            self.instance.save()
            EquipmentModelSpecification.objects.create(
                model=self.instance,
                specification_type=ContentType.objects.get_for_model(model),
                specification_id=specification.id
            )

        def update():
            for field in models_fields:
                if model == AcousticDetectorSpecification and field == 'detected_labels':
                    s: AcousticDetectorSpecification
                    for label in spec.specification.detected_labels.filter(
                            ~Q(id__in=models_fields[field].values_list('id', flat=True))):
                        spec.specification.detected_labels.remove(label)
                    for label in models_fields[field]:
                        if not spec.specification.detected_labels.filter(id=label.id).exists():
                            spec.specification.detected_labels.add(label)
                else:
                    setattr(spec.specification, field, models_fields[field])
            spec.save()

        def remove():
            rel.delete()
            if not other_rels.exists():
                spec.delete()

        if not commit:
            return

        if not should_exists:
            if spec is None:  # No changes
                return
            return remove()

        if spec is None:
            return create()

        is_updated = False
        for field in models_fields:
            if getattr(spec.specification, field) != models_fields[field]:
                is_updated = True

        if is_updated and other_rels.exists():
            return create()

        update()
