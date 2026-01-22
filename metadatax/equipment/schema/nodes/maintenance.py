import graphene
from django_extension.schema.types import ExtendedNode

from metadatax.common.schema import PersonNode, InstitutionNode
from metadatax.equipment.models import Maintenance
from .maintenance_type import MaintenanceTypeNode


class MaintenanceNode(ExtendedNode):
    type = graphene.NonNull(MaintenanceTypeNode)

    maintainer = graphene.NonNull(PersonNode)
    maintainer_institution = graphene.NonNull(InstitutionNode)

    class Meta:
        model = Maintenance
        fields = "__all__"
        filter_fields = {
            "id": ["exact", "in"],
            "type_id": ["exact", "in"],
            "maintainer_id": ["exact", "in"],
            "maintainer_institution_id": ["exact", "in"],
            "platform_id": ["exact", "in"],
            "equipment_id": ["exact", "in"],
            "date": ["exact", "lt", "lte", "gt", "gte"],
        }
