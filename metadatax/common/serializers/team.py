from rest_framework import serializers

from metadatax.common.models import Team
from .institution import InstitutionSerializer


class TeamSerializer(serializers.ModelSerializer):
    institution = InstitutionSerializer()

    class Meta:
        model = Team
        fields = "__all__"
