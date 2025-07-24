from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from metadatax.common.models import Institution
from metadatax.utils import custom_fields
from .acoustic_detector_specification import AcousticDetectorSpecification
from .hydrophone_specification import HydrophoneSpecification
from .recorder_specification import RecorderSpecification
from .storage_specification import StorageSpecification


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

    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    owner = models.ForeignKey(
        Institution, on_delete=models.PROTECT, related_name="owned_equipments"
    )
    provider = models.ForeignKey(
        Institution, on_delete=models.PROTECT, related_name="provided_equipments"
    )

    storage_specification = models.ForeignKey(
        StorageSpecification, on_delete=models.PROTECT, blank=True, null=True
    )
    recorder_specification = models.ForeignKey(
        RecorderSpecification, on_delete=models.PROTECT, blank=True, null=True
    )
    hydrophone_specification = models.ForeignKey(
        HydrophoneSpecification, on_delete=models.PROTECT, blank=True, null=True
    )
    acoustic_detector_specification = models.ForeignKey(
        AcousticDetectorSpecification, on_delete=models.PROTECT, blank=True, null=True
    )

    purchase_date = custom_fields.DateField(null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    battery_slots_count = models.IntegerField(null=True, blank=True)
    battery_type = models.CharField(max_length=100, null=True, blank=True)
    cables = models.TextField(null=True, blank=True)


@receiver(post_delete, sender=Equipment)
def delete_specifications(sender, instance: Equipment, **kwargs):
    if instance.storage_specification is not None:
        instance.storage_specification.delete()
    if instance.recorder_specification is not None:
        (instance.recorder_specification.delete())
    if instance.hydrophone_specification is not None:
        instance.hydrophone_specification.delete()
    if instance.acoustic_detector_specification is not None:
        instance.acoustic_detector_specification.delete()
