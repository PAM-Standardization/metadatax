import graphene
from django_extension.schema.types import ExtendedNode

from metadatax.common.schema import InstitutionNode
from metadatax.common.schema.unions import ContactUnion
from metadatax.equipment.models import Platform
from .platform_type import PlatformTypeNode


class PlatformNode(ExtendedNode):
    type = graphene.NonNull(PlatformTypeNode)
    provider = graphene.NonNull(InstitutionNode)

    class Meta:
        model = Platform
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "owner_id": ["exact", "in"],
            "provider_id": ["exact", "in"],
            "name": ["exact", "icontains"],
        }

    owner = ContactUnion()

    def resolve_owner(self: Platform, info):
        return self.owner
