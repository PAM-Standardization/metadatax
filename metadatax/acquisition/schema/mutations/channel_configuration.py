from django import forms
import graphene
from graphene import Field
from graphene_django.forms.mutation import DjangoModelFormMutation

from metadatax.acquisition.models import ChannelConfiguration
from ..nodes import ChannelConfigurationNode
from .deployment import DeploymentInput
from .recorder_specification import ChannelConfigurationRecorderSpecificationInput
from .detector_specification import ChannelConfigurationDetectorSpecificationInput


class ChannelConfigurationInput(graphene.InputObjectType):
    deployment = graphene.NonNull(DeploymentInput)

    is_lost = graphene.Boolean(required=False)

    recorder_specification = ChannelConfigurationRecorderSpecificationInput()
    detector_specification = ChannelConfigurationDetectorSpecificationInput()
    storages = graphene.List(graphene.ID, required=False)

    continuous = graphene.Boolean(required=False)
    duty_cycle_on = graphene.Int(required=False)
    duty_cycle_off = graphene.Int(required=False)

    instrument_depth = graphene.Int(required=False)

    timezone = graphene.String(required=False)
    record_start_date = graphene.DateTime(required=False)
    record_end_date = graphene.DateTime(required=False)

    extra_information = graphene.String(required=False)


class ChannelConfigurationForm(forms.ModelForm):
    class Meta:
        model = ChannelConfiguration
        fields = '__all__'
        widgets = {
            'record_start_date': forms.TextInput(),
            'record_end_date': forms.TextInput(),
        }


class ChannelConfigurationMutation(DjangoModelFormMutation):
    channel_configuration = Field(ChannelConfigurationNode)

    class Meta:
        form_class = ChannelConfigurationForm
