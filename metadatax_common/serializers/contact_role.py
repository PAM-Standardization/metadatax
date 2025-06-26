from rest_framework import serializers

from metadatax_common.models import ContactRole
from utils.serializers import EnumField
from .contact import ContactSerializer


class ContactRoleSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    role = EnumField(ContactRole.Type)

    class Meta:
        model = ContactRole
        fields = "__all__"
