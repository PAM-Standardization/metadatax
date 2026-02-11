import graphene
import graphene_django_optimizer
from django_extension.schema.types import ExtendedNode

from metadatax.common.schema import AccessibilityEnum
from metadatax.data.models import DetectionFile


class DetectionFileNode(ExtendedNode):
    accessibility = AccessibilityEnum()

    class Meta:
        model = DetectionFile
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "filename": ["exact", "icontains"],
            "storage_location": ["exact", "icontains"],
            "file_size": ["exact", "lt", "lte", "gt", "gte"],
            "accessibility": ["exact"],
        }

    start = graphene.Int(required=True)

    @graphene_django_optimizer.resolver_hints()
    def resolve_start(self: DetectionFile, info):
        return self.detection_properties.start

    end = graphene.Int(required=True)

    @graphene_django_optimizer.resolver_hints()
    def resolve_end(self: DetectionFile, info):
        return self.detection_properties.end
