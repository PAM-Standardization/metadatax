from django import forms
import graphene
from graphene import Field
from graphene_django.forms.mutation import DjangoModelFormMutation

from metadatax.acquisition.models import Deployment
from metadatax.common.schema.mutations.contact import ContactInput
from metadatax.data.schema.mutations.visual_observation import VisualObservationInput
from ..nodes import DeploymentNode


class DeploymentInput(graphene.InputObjectType):
    project = graphene.ID(required=True)
    longitude = graphene.Float(required=True)
    latitude = graphene.Float(required=True)

    name = graphene.String(required=False)
    site = graphene.String(required=False)
    campaign = graphene.String(required=False)
    platform = graphene.ID(required=False)
    bathymetric_depth = graphene.Int(required=False)
    deployment_date = graphene.DateTime(required=False)
    deployment_vessel = graphene.String(required=False)
    recovery_date = graphene.DateTime(required=False)
    recovery_vessel = graphene.String(required=False)
    contacts = graphene.List(ContactInput)
    description = graphene.String(required=False)

    visual_observations = graphene.List(VisualObservationInput)


class DeploymentForm(forms.ModelForm):
    class Meta:
        model = Deployment
        fields = '__all__'
        widgets = {
            "deployment_date": forms.DateTimeInput,
            "recovery_date": forms.DateTimeInput,
        }


class DeploymentMutation(DjangoModelFormMutation):
    deployment = Field(DeploymentNode)

    class Meta:
        form_class = DeploymentForm
