from rest_framework import serializers

from metadatax.equipment.models import RecorderSpecification


class RecorderSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecorderSpecification
        fields = '__all__'
