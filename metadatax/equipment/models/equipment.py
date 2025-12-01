from django.db import models

from metadatax.common.models import Institution
from metadatax.utils import custom_fields
from .equipment_model import EquipmentModel


class Equipment(models.Model):
    """Equipment model"""

    class Meta:
        unique_together = ["model", "serial_number"]
        db_table = "metadatax_equipment_equipment"
        ordering = ("name", "model", "serial_number")

    def __str__(self):
        if self.name is not None:
            return f"{self.name} (owner: {self.owner})"
        return f"{self.model} ({self.serial_number} ; owner: {self.owner})"

    model = models.ForeignKey(EquipmentModel, related_name="equipments", on_delete=models.PROTECT)
    serial_number = models.CharField(max_length=100)
    owner = models.ForeignKey(
        Institution, on_delete=models.PROTECT, related_name="owned_equipments"
    )

    purchase_date = custom_fields.DateField(null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    sensitivity = models.FloatField(null=True, blank=True, help_text="Required only for hydrophones")
