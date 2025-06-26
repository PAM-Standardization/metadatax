import datetime

from django.db import models

from metadatax_common.models import Contact
from .equipment import Equipment
from .maintenance_type import MaintenanceType
from .platform import Platform


class Maintenance(models.Model):
    class Meta:
        unique_together = ["type", "date", "platform", "equipment"]
        constraints = [
            models.CheckConstraint(
                name="maintenance_concern_platform_or_equipment",
                check=models.Q(platform__isnull=False, equipment__isnull=True)
                      | models.Q(platform__isnull=True, equipment__isnull=False),
            )
        ]

    def __str__(self):
        return f"{self.date}: {self.type}"

    type = models.ForeignKey(MaintenanceType, on_delete=models.CASCADE, related_name='maintenances')
    date = models.DateField(default=datetime.date.today)

    description = models.TextField(blank=True, null=True)
    maintainer = models.ForeignKey(
        Contact, on_delete=models.PROTECT,
        related_name='performed_maintenances',
        blank=True, null=True,
    )

    platform = models.ForeignKey(
        Platform, on_delete=models.CASCADE,
        related_name='maintenances',
        blank=True, null=True,
    )
    equipment = models.ForeignKey(
        Equipment, on_delete=models.CASCADE,
        related_name='maintenances',
        blank=True, null=True,
    )
