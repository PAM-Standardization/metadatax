from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from metadatax.common.models import Institution


class EquipmentModel(models.Model):
    """Equipment model"""

    class Meta:
        unique_together = ["name", "provider"]
        db_table = "mx_equipment_equipmentmodel"
        ordering = ("name",)

    def __str__(self):
        return f"{self.provider.name} {self.name}"

    name = models.CharField(
        max_length=100,
        help_text="Name of the model",
    )
    provider = models.ForeignKey(
        Institution, on_delete=models.PROTECT, related_name="provided_equipments"
    )

    battery_slots_count = models.IntegerField(
        null=True,
        blank=True,
        help_text="Number of battery slots",
    )
    battery_type = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Type of battery supported by the model",
    )
    cables = models.TextField(
        null=True,
        blank=True,
        help_text="List of cables required to use the model",
    )


class EquipmentModelSpecification(models.Model):
    class Meta:
        db_table = "mx_equipment_equipmentmodel_specification"
        indexes = [
            models.Index(fields=["specification_type", "specification_id"]),
        ]

    def __str__(self):
        return f"{self.model.__str__()} - {self.specification_type.model} [{self.specification_id}]"

    model = models.ForeignKey(EquipmentModel, on_delete=models.CASCADE, related_name="specification_relations")

    specification_type = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT,
        limit_choices_to={
            "model__in": [
                "AcousticDetectorSpecification".lower(),
                "HydrophoneSpecification".lower(),
                "RecorderSpecification".lower(),
                "StorageSpecification".lower(),
            ]
        },
    )
    specification_id = models.PositiveBigIntegerField()
    specification = GenericForeignKey("specification_type", "specification_id")
