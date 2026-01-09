from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from metadatax.utils import custom_fields
from .equipment_model import EquipmentModel


class Equipment(models.Model):
    """Equipment model"""

    class Meta:
        unique_together = ["model", "serial_number"]
        db_table = "mx_equipment_equipment"
        ordering = ("name", "model", "serial_number")

    def __str__(self):
        return f"{self.model} ({self.name or f"#{self.serial_number}"})"

    model = models.ForeignKey(EquipmentModel, related_name="equipments", on_delete=models.PROTECT)
    serial_number = models.CharField(max_length=100)

    owner_type = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT,
        limit_choices_to={
            "model__in": [
                "common.Person",
                "common.Team",
                "common.Institution",
            ]
        },
    )
    owner_id = models.PositiveBigIntegerField()
    owner = GenericForeignKey("owner_type", "owner_id")

    purchase_date = custom_fields.DateField(null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    sensitivity = models.FloatField(null=True, blank=True, help_text="Required only for hydrophones")
