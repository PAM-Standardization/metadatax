from rest_framework import serializers

from metadatax.common.models import Person
from .institution import InstitutionSerializer
from .team import TeamSerializer


class PersonSerializer(serializers.ModelSerializer):
    initial_names = serializers.CharField(read_only=True)

    institutions = InstitutionSerializer(many=True)
    teams = TeamSerializer(many=True)

    class Meta:
        model = Person
        fields = "__all__"
