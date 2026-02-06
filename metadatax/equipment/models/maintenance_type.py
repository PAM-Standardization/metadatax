from django.db import models

from metadatax.utils import custom_fields
from metadatax.utils.custom_fields.duration import duration_to_readable_year_month_day


class MaintenanceType(models.Model):
    class Meta:
        db_table = "mx_equipment_maintenancetype"

    def __str__(self):
        s = self.name
        if self.interval is not None:
            s += f" (every {self._interval})"
        return s

    name = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True,
        help_text='Name of the maintenance type',
    )

    description = models.TextField(
        blank=True,
        null=True,
        help_text='Description of this type of maintenance',
    )
    interval = custom_fields.DurationField(
        blank=True,
        null=True,
        help_text="Recommended interval of execution for this type of maintenance",
    )

    @property
    def _interval(self):
        return duration_to_readable_year_month_day(self.interval)
