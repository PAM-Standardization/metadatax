import graphene
from django_extension.schema.types import ExtendedNode

from metadatax.acquisition.models import Project
from metadatax.common.schema import AccessibilityEnum, ContactRelationNode
from ..enums import FinancingEnum


class ProjectNode(ExtendedNode):
    accessibility = AccessibilityEnum()
    financing = FinancingEnum()
    contacts = graphene.List(ContactRelationNode)

    class Meta:
        model = Project
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
            "accessibility": ["exact"],
            "doi": ["exact"],
            "start_date": ["exact", "lte", "lt", "gte", "gt"],
            "end_date": ["exact", "lte", "lt", "gte", "gt"],
            "project_goal": ["exact", "icontains"],
            "financing": ["exact"],
        }
