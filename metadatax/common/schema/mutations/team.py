from django import forms
from graphene import Field
from graphene_django.forms.mutation import DjangoModelFormMutation

from metadatax.common.models import Team
from ..nodes import TeamNode


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'


class TeamMutation(DjangoModelFormMutation):
    Team = Field(TeamNode)

    class Meta:
        form_class = TeamForm
