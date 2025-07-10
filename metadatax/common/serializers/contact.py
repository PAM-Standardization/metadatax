from rest_framework import serializers

from metadatax.common.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    initial_names = serializers.CharField(read_only=True)

    class Meta:
        model = Contact
        fields = "__all__"
