from django_filters import FilterSet, NumberFilter
from graphene import ID, relay
from metadatax.acquisition.models import Project
from metadatax.common.schema import AccessibilityEnum

from .enums import FinancingEnum
from ...utils.schema import MxObjectType


class ProjectFilter(FilterSet):

    contacts__id = NumberFilter()
    project_type__id = NumberFilter()
    project_type = NumberFilter(field_name="project_type__name")
    campaigns__id = NumberFilter()
    sites__id = NumberFilter()
    deployments__id = NumberFilter()

    class Meta:
        model = Project
        fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
            "contacts__id": ["exact", "in"],
            "project_type__id": ["exact", "in"],
            "campaigns__id": ["exact", "in"],
            "sites__id": ["exact", "in"],
            "deployments__id": ["exact", "in"],
            "project_type": ["exact"],
            "accessibility": ["exact"],
            "doi": ["exact"],
            "start_date": ["exact", "lte", "lt", "gte", "gt"],
            "end_date": ["exact", "lte", "lt", "gte", "gt"],
            "project_goal": ["exact", "icontains"],
            "financing": ["exact"],
        }


class ProjectNode(MxObjectType):
    id = ID(required=True)
    accessibility = AccessibilityEnum()
    financing = FinancingEnum()

    class Meta:
        model = Project
        fields = "__all__"
        filter_fields = {}
        # filterset_class = ProjectFilter
        interfaces = (relay.Node,)
