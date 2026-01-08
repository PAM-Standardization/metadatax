from django.db import models

from metadatax.utils import custom_fields


class StorageSpecification(models.Model):
    """Storage Specification model"""

    class Meta:
        db_table = "mx_equipment_storagespecification"
        unique_together = ("capacity", "type")
        ordering = ("-capacity",)

    def __str__(self):
        if self.capacity is None:
            return super().__str__()
        info = [str(self.capacity)]
        if self.type:
            info.append(self.type)
        return ", ".join(info)

    capacity = custom_fields.ByteField()
    type = models.CharField(max_length=100, blank=True, null=True)
