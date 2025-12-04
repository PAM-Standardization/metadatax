from graphene import relay, ID

from metadatax.common.models import Institution
from metadatax.utils.schema import MxObjectType


class InstitutionNode(MxObjectType):
    id = ID(required=True)

    class Meta:
        model = Institution
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
            "city": ["exact", "icontains"],
            "country": ["exact", "icontains"],
            "mail": ["exact", "icontains"],
            "website": ["exact", "icontains"],
        }
        interfaces = (relay.Node,)
