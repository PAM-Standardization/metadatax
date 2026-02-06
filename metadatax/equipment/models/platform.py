from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from metadatax.common.models import Institution
from .platform_type import PlatformType


class Platform(models.Model):
    """Platform model"""

    class Meta:
        unique_together = ["owner_type", "owner_id", "provider", "type", "name"]
        db_table = "mx_equipment_platform"

    def __str__(self):
        if self.name:
            return self.name
        return f"{self.type} (owner: {self.owner} ; provider: {self.provider})"

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
        blank=True, null=True
    )
    owner_id = models.PositiveBigIntegerField(
        blank=True, null=True
    )
    owner = GenericForeignKey("owner_type", "owner_id")

    provider = models.ForeignKey(
        Institution, on_delete=models.PROTECT, related_name="provided_platforms",
        blank=True, null=True
    )
    type = models.ForeignKey(
        PlatformType, on_delete=models.PROTECT, related_name="platforms"
    )

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Name of the platform",
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Description of the platform",
    )
