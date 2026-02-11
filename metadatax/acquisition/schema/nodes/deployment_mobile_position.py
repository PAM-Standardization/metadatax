from django_extension.schema.types import ExtendedNode

from metadatax.acquisition.models import DeploymentMobilePosition


class DeploymentMobilePositionNode(ExtendedNode):
    class Meta:
        model = DeploymentMobilePosition
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "deployment_id": ["exact", "in"],
            "datetime": ["exact", "lt", "lte", "gt", "gte"],
            "longitude": ["exact", "lt", "lte", "gt", "gte"],
            "latitude": ["exact", "lt", "lte", "gt", "gte"],
            "depth": ["exact", "lt", "lte", "gt", "gte"],
            "heading": ["exact", "lt", "lte", "gt", "gte"],
            "pitch": ["exact", "lt", "lte", "gt", "gte"],
            "roll": ["exact", "lt", "lte", "gt", "gte"],
        }
