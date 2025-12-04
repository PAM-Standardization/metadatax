from rest_framework import serializers

from metadatax.common.models.relations import ContactRelation


class ContactRoleSerializer(serializers.ModelSerializer):
    # TODO!

    class Meta:
        model = ContactRelation
        fields = "__all__"
