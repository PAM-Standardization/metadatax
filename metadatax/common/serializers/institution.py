from rest_framework import serializers

from metadatax.common.models import Institution


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = "__all__"
