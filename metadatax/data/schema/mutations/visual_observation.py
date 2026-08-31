from django import forms
import graphene
from graphene import Field
from graphene_django.forms.mutation import DjangoModelFormMutation

from metadatax.data.models import VisualObservation
from ..nodes import VisualObservationNode


class VisualObservationInput(graphene.InputObjectType):
    source = graphene.ID(required=True)
    start_datetime = graphene.DateTime(required=True)
    end_datetime = graphene.DateTime(required=True)

    count_min = graphene.Int(required=False)
    count_max = graphene.Int(required=False)
    start_distance_min = graphene.Int(required=False)
    start_distance_max = graphene.Int(required=False)
    end_distance_min = graphene.Int(required=False)
    end_distance_max = graphene.Int(required=False)
    young_presence = graphene.Boolean(required=False)
    other_human_activity_presence = graphene.Boolean(required=False)
    behaviors = graphene.List(graphene.ID, required=False)
    reactions_to_boat = graphene.List(graphene.ID, required=False)

    additional_information = graphene.String(required=False)


class VisualObservationForm(forms.ModelForm):
    class Meta:
        model = VisualObservation
        fields = '__all__'
        widgets = {
            'start_datetime': forms.TextInput(),
            'end_datetime': forms.TextInput(),
        }


class VisualObservationMutation(DjangoModelFormMutation):
    VisualObservation = Field(VisualObservationNode)

    class Meta:
        form_class = VisualObservationForm
