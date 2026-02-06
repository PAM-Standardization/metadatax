from django.db import models

from metadatax.utils import custom_fields


class RecorderSpecification(models.Model):
    """Recorder Specification model"""

    class Meta:
        db_table = "mx_equipment_recorderspecification"
        unique_together = (
            "channels_count",
            "storage_slots_count",
            "storage_maximum_capacity",
            "storage_type",
        )

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

    def __eq__(self, other: "RecorderSpecification") -> bool:
        return (self.channels_count == other.channels_count and
                self.storage_slots_count == other.storage_slots_count and
                self.storage_maximum_capacity == other.storage_maximum_capacity and
                self.storage_type == other.storage_type)

    channels_count = models.IntegerField(
        blank=True,
        null=True,
        help_text="Number of all the channels on the recorder, even if unused.",
    )
    storage_slots_count = models.IntegerField(
        blank=True,
        null=True,
        help_text="Number of all the storage slots on the recorder.",
    )
    storage_maximum_capacity = custom_fields.ByteField(
        blank=True,
        null=True,
        help_text="Maximum storage capacity supported by the recorder.",
    )
    storage_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Type of storage supported by the recorder.",
    )
