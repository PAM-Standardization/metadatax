from rest_framework import serializers

from metadatax.common.models import ContactRole
from metadatax.utils import EnumField
from .contact import ContactSerializer


class ContactRoleSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    role = EnumField(ContactRole.Type)

    class Meta:
        model = ContactRole
        fields = "__all__"
