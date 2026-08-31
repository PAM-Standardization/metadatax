from django import forms
import graphene

from metadatax.acquisition.models.channel_configuration_specifications import ChannelConfigurationDetectorSpecification


class ChannelConfigurationDetectorSpecificationInput(graphene.InputObjectType):
    detector = graphene.ID(required=True)
    output_formats = graphene.List(graphene.ID, required=True)
    labels = graphene.List(graphene.ID, required=True)  # TODO: check labels are in detector detected labels

    min_frequency = graphene.Int(required=False)
    max_frequency = graphene.Int(required=False)
    filter = graphene.String(required=False)
    configuration = graphene.String(required=False)


class ChannelConfigurationDetectorSpecificationForm(forms.ModelForm):
    class Meta:
        model = ChannelConfigurationDetectorSpecification
        fields = '__all__'
