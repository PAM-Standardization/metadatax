from django import forms
from django.contrib.contenttypes.models import ContentType
from graphene import Field
from graphene_django.forms.mutation import DjangoModelFormMutation

from metadatax.equipment.models import Equipment
from ..nodes import EquipmentNode


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'


class EquipmentMutation(DjangoModelFormMutation):
    Equipment = Field(EquipmentNode)

    class Meta:
        form_class = EquipmentForm

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        input['owner_type'] = ContentType.objects.get(
            app_label="common",
            model=input['owner_type']
        )
        return super().mutate_and_get_payload(root, info, **input)
