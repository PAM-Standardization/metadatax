from django_extension.schema.types import ExtendedNode

from metadatax.acquisition.models import Site


class SiteNode(ExtendedNode):
    class Meta:
        model = Site
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
            "project_id": ["exact", "in"],
        }
