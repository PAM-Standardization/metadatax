import graphene
from django import forms
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from graphene_django.types import ErrorType
from metadatax.equipment.forms import AcousticDetectorSpecificationForm, RecorderSpecificationForm, \
    HydrophoneSpecificationForm, \
    StorageSpecificationForm
from metadatax.equipment.models import EquipmentModel, EquipmentModelSpecification

from .specifications import AcousticDetectorSpecificationInput, RecorderSpecificationInput, \
    HydrophoneSpecificationInput, StorageSpecificationInput
from ..nodes import EquipmentModelNode


class EquipmentModelForm(forms.ModelForm):
    class Meta:
        model = EquipmentModel
        fields = '__all__'


class EquipmentModelInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    provider = graphene.ID(required=True)

    battery_slots_count = graphene.Int(required=False)
    battery_type = graphene.String(required=False)
    cables = graphene.String(required=False)

    acoustic_detector_specification = AcousticDetectorSpecificationInput()
    recorder_specification = RecorderSpecificationInput()
    hydrophone_specification = HydrophoneSpecificationInput()
    storage_specification = StorageSpecificationInput()


class CreateEquipmentModel(graphene.Mutation):
    """Create a Equipment model with its specifications"""

    class Arguments:
        input = graphene.NonNull(EquipmentModelInput)

    equipment_model = graphene.Field(EquipmentModelNode)
    errors = graphene.List(ErrorType)

    @classmethod
    @transaction.atomic
    def mutate(cls, root, info, input):
        acoustic_detector_specification_data = input.pop("acoustic_detector_specification", None)
        recorder_specification_data = input.pop("recorder_specification", None)
        hydrophone_specification_data = input.pop("hydrophone_specification", None)
        storage_specification_data = input.pop("storage_specification", None)

        model_form = EquipmentModelForm(data=dict(input))

        if not model_form.is_valid():
            errors = [
                ErrorType(field=field, messages=messages)
                for field, messages in model_form.errors.items()
            ]
            return cls(equipment_model=None, errors=errors)

        model: EquipmentModel = model_form.save()
        specs = []
        errors = []

        if acoustic_detector_specification_data is not None:
            spec_form = AcousticDetectorSpecificationForm(data=dict(acoustic_detector_specification_data))
            if spec_form.is_valid():
                specs.append(spec_form.save())
            else:
                for field, messages in spec_form.errors.items():
                    errors.append(ErrorType(field=f"acoustic_detector_specification-{field}", messages=messages))

        if recorder_specification_data is not None:
            recorder_specification_data['storage_maximum_capacity_0'] = recorder_specification_data.pop("storage_maximum_capacity_amount", None)
            recorder_specification_data['storage_maximum_capacity_1'] = recorder_specification_data.pop("storage_maximum_capacity_unit", None)
            spec_form = RecorderSpecificationForm(data=dict(recorder_specification_data))

            if spec_form.is_valid():
                specs.append(spec_form.save())
            else:
                for field, messages in spec_form.errors.items():
                    errors.append(ErrorType(field=f"recorder_specification-{field}", messages=messages))

        if hydrophone_specification_data is not None:
            spec_form = HydrophoneSpecificationForm(data=dict(hydrophone_specification_data))
            if spec_form.is_valid():
                specs.append(spec_form.save())
            else:
                for field, messages in spec_form.errors.items():
                    errors.append(ErrorType(field=f"hydrophone_specification-{field}", messages=messages))

        if storage_specification_data is not None:
            storage_specification_data['capacity_0'] = storage_specification_data.pop("capacity_amount", None)
            storage_specification_data['capacity_1'] = storage_specification_data.pop("capacity_unit", None)
            spec_form = StorageSpecificationForm(data=dict(storage_specification_data))
            if spec_form.is_valid():
                specs.append(spec_form.save())
            else:
                for field, messages in spec_form.errors.items():
                    errors.append(ErrorType(field=f"storage_specification-{field}", messages=messages))

        if len(errors) > 0:
            model.delete()
            return cls(equipment_model=None, errors=errors)

        for spec in specs:
            EquipmentModelSpecification.objects.create(
                model=model,
                specification_type=ContentType.objects.get_for_model(spec),
                specification_id=spec.id,
            )

        return cls(equipment_model=model)
