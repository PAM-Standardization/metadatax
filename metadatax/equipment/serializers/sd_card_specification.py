from rest_framework import serializers

from metadatax.equipment.models import SDCardSpecification


class SDCardSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SDCardSpecification
        fields = '__all__'
