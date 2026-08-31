from django import forms
import graphene
from graphene import Field
from graphene_django.forms.mutation import DjangoModelFormMutation

from metadatax.acquisition.models.channel_configuration_specifications import ChannelConfigurationRecorderSpecification
from ..nodes.channel_configuration_specifications import ChannelConfigurationRecorderSpecificationNode


class ChannelConfigurationRecorderSpecificationInput(graphene.InputObjectType):
    recorder = graphene.ID(required=True)
    hydrophone = graphene.ID(required=True)
    recording_formats = graphene.List(graphene.ID, required=True)
    sampling_frequency = graphene.Int(required=True)
    sample_depth = graphene.Int(required=True)
    gain = graphene.Float(required=True)
    channel_name = graphene.String(required=False)


class ChannelConfigurationRecorderSpecificationForm(forms.ModelForm):
    class Meta:
        model = ChannelConfigurationRecorderSpecification
        fields = '__all__'


class ChannelConfigurationRecorderSpecificationMutation(DjangoModelFormMutation):
    recorder_specification = Field(ChannelConfigurationRecorderSpecificationNode)

    class Meta:
        form_class = ChannelConfigurationRecorderSpecificationForm
