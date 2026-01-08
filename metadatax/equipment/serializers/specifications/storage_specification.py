from rest_framework import serializers

from metadatax.equipment.models import StorageSpecification


class StorageSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageSpecification
        fields = "__all__"
