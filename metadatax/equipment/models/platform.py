from django.db import models

from metadatax.common.models import Institution
from .platform_type import PlatformType


class Platform(models.Model):
    """Platform model"""

    class Meta:
        unique_together = ['owner', 'provider', 'type', 'name']
        db_table = 'metadatax_equipment_platform'

    def __str__(self):
        if self.name:
            return self.name
        return f"{self.type} (owner: {self.owner} ; provider: {self.provider})"

    owner = models.ForeignKey(Institution, on_delete=models.PROTECT, related_name='owned_platforms')
    provider = models.ForeignKey(Institution, on_delete=models.PROTECT, related_name='provided_platforms')
    type = models.ForeignKey(PlatformType, on_delete=models.PROTECT, related_name='platforms')

    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
