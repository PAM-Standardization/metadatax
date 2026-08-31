from django.contrib.contenttypes.models import ContentType
from django.db.models import QuerySet, Exists, OuterRef
from django_extension.filters import ExtendedFilterSet
from django_extension.schema.types import ExtendedNode
from django_filters import BooleanFilter
from graphene import String
import graphene_django_optimizer

from metadatax.common.schema.unions import ContactUnion
from metadatax.equipment.models import Equipment, EquipmentModelSpecification, StorageSpecification, \
    RecorderSpecification, HydrophoneSpecification, AcousticDetectorSpecification
from .equipment_model import EquipmentModelNode


class EquipmentFilterSet(ExtendedFilterSet):
    is_storage = BooleanFilter(method="filter_is_storage")
    is_recorder = BooleanFilter(method="filter_is_recorder")
    is_hydrophone = BooleanFilter(method="filter_is_hydrophone")
    is_detector = BooleanFilter(method="filter_is_detector")

    class Meta:
        model = Equipment
        fields = {
            "id": ["exact", "in"],
            "serial_number": ["exact", "icontains"],
            "purchase_date": ["exact", "lt", "lte", "gt", "gte"],
            "name": ["exact", "icontains"],
            "sensitivity": ["exact", "lt", "lte", "gt", "gte", "isnull"],
        }

    def filter_is_storage(self, queryset: QuerySet[Equipment], name, value: bool):
        return queryset.filter(
            Exists(
                EquipmentModelSpecification.objects.filter(
                    specification_type=ContentType.objects.get_for_model(StorageSpecification),
                    model_id=OuterRef("model_id"),
                )
            )
        )

    def filter_is_recorder(self, queryset: QuerySet[Equipment], name, value: bool):
        return queryset.filter(
            Exists(
                EquipmentModelSpecification.objects.filter(
                    specification_type=ContentType.objects.get_for_model(RecorderSpecification),
                    model_id=OuterRef("model_id"),
                )
            )
        )

    def filter_is_hydrophone(self, queryset: QuerySet[Equipment], name, value: bool):
        return queryset.filter(
            Exists(
                EquipmentModelSpecification.objects.filter(
                    specification_type=ContentType.objects.get_for_model(HydrophoneSpecification),
                    model_id=OuterRef("model_id"),
                )
            )
        )

    def filter_is_detector(self, queryset: QuerySet[Equipment], name, value: bool):
        return queryset.filter(
            Exists(
                EquipmentModelSpecification.objects.filter(
                    specification_type=ContentType.objects.get_for_model(AcousticDetectorSpecification),
                    model_id=OuterRef("model_id"),
                )
            )
        )


class EquipmentNode(ExtendedNode):
    model = EquipmentModelNode()

    class Meta:
        model = Equipment
        fields = "__all__"
        filterset_class = EquipmentFilterSet

    owner = ContactUnion()

    def resolve_owner(self: Equipment, info):
        return self.owner

    display_name = String(required=True)

    @graphene_django_optimizer.resolver_hints()
    def resolve_display_name(self: Equipment, info):
        return self.__str__()
