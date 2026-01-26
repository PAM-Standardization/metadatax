from django.contrib.contenttypes.models import ContentType
from django_extension.serializers import EnumField
from rest_framework import serializers

from metadatax.common.models import ContactRelation, Person, Team, Institution, Role
from .person import PersonSerializer
from .team import TeamSerializer
from .institution import InstitutionSerializer


class ContactRelatedField(serializers.RelatedField):
    def to_representation(self, obj):
        if isinstance(obj, Person):
            return PersonSerializer(obj).data
        elif isinstance(obj, Team):
            return TeamSerializer(obj).data
        elif isinstance(obj, Institution):
            return InstitutionSerializer(obj).data
        raise Exception('Unexpected type of object')

class ContactRoleSerializer(serializers.ModelSerializer):
    role = EnumField(Role)
    contact = ContactRelatedField(read_only=True)
    contact_type = serializers.SlugRelatedField(
        queryset=ContentType.objects.all(),
        slug_field='model',
    )

    class Meta:
        model = ContactRelation
        exclude = ('contact_id',)
