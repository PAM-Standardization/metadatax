from django.db import models

from metadatax.utils import custom_fields


class RecorderSpecification(models.Model):
    """Recorder Specification model"""

    class Meta:
        db_table = "metadatax_equipment_recorderspecification"

    def __str__(self):
        info = [f"{self.channels_count} channels"]
        storage_info = []
        if self.storage_slots_count:
            storage_info.append(f"{self.storage_slots_count} sd slots")
        if self.storage_maximum_capacity:
            storage_info.append(f"<{self.storage_maximum_capacity}")
        if self.storage_type:
            storage_info.append(self.storage_type)
        if len(storage_info) > 0:
            info.append(f"({', '.join(storage_info)})")
        return ", ".join(info)

    channels_count = models.IntegerField(
        blank=True,
        null=True,
        help_text="Number of all the channels on the recorder, even if unused.",
    )
    storage_slots_count = models.IntegerField(blank=True, null=True)
    storage_maximum_capacity = custom_fields.ByteField(blank=True, null=True)
    storage_type = models.CharField(max_length=100, blank=True, null=True)
