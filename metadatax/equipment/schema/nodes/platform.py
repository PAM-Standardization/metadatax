import graphene
from django_extension.schema.types import ExtendedNode
from graphene import String
import graphene_django_optimizer

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

    @graphene_django_optimizer.resolver_hints()
    def resolve_owner(self: Platform, info):
        return self.owner

    display_name = String(required=True)

    @graphene_django_optimizer.resolver_hints()
    def resolve_display_name(self: Platform, info):
        return self.__str__()
