from django_extension.schema.types import ExtendedNode

from metadatax.common.models import Institution


class InstitutionNode(ExtendedNode):
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