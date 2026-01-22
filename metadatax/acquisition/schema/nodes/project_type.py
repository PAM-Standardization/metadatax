from django_extension.schema.types import ExtendedNode

from metadatax.acquisition.models import ProjectType


class ProjectTypeNode(ExtendedNode):
    class Meta:
        model = ProjectType
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
        }
