from django_extension.schema.types import ExtendedNode

from metadatax.ontology.models import Source


class SourceNode(ExtendedNode):
    class Meta:
        model = Source
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "parent_id": ["exact", "in"],
            "english_name": ["exact", "icontains"],
            "latin_name": ["exact", "icontains"],
            "french_name": ["exact", "icontains"],
            "code_name": ["exact", "icontains"],
            "taxon": ["exact", "icontains"],
        }
