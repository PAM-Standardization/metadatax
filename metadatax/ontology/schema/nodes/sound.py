from django_extension.schema.types import ExtendedNode

from metadatax.ontology.models import Sound


class SoundNode(ExtendedNode):
    class Meta:
        model = Sound
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "parent_id": ["exact", "in"],
            "english_name": ["exact", "icontains"],
            "french_name": ["exact", "icontains"],
            "code_name": ["exact", "icontains"],
            "taxon": ["exact", "icontains"],
        }
