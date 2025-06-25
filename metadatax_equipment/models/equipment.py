from django.db import models
from django.db.models import CheckConstraint
from django.db.models.signals import post_delete
from django.dispatch import receiver

from metadatax_common.models import Contact
from .acoustic_detector_specification import AcousticDetectorSpecification
from .hydrophone_specification import HydrophoneSpecification
from .recorder_specification import RecorderSpecification
from .sd_card_specification import SDCardSpecification


class Equipment(models.Model):
    """Equipment model"""

    class Meta:
        unique_together = ["model", "serial_number"]
        constraints = [
            CheckConstraint(
                name="sd_card_is_only_sd_card",
                check=models.Q(sd_card_specification__isnull=False, recorder_specification__isnull=True,
                               hydrophone_specification__isnull=True, acoustic_detector_specification__isnull=True)
                      | models.Q(sd_card_specification__isnull=True),
            )
        ]

    def __str__(self):
        if self.name is not None:
            return f"{self.name} (owner: {self.owner})"
        return f"{self.model} ({self.serial_number} ; owner: {self.owner})"

    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    owner = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='owned_equipments')
    provider = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='provided_equipments')

    sd_card_specification = models.OneToOneField(
        SDCardSpecification,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    recorder_specification = models.OneToOneField(
        RecorderSpecification,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    hydrophone_specification = models.OneToOneField(
        HydrophoneSpecification,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    acoustic_detector_specification = models.OneToOneField(
        AcousticDetectorSpecification,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )

    purchase_date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=100)
    battery_slots_count = models.IntegerField(null=True, blank=True)
    battery_type = models.CharField(max_length=100, null=True, blank=True)
    cables = models.TextField(null=True, blank=True)


@receiver(post_delete, sender=Equipment)
def delete_specifications(sender, instance: Equipment, **kwargs):
    if instance.sd_card_specification is not None:
        instance.sd_card_specification.delete()
    if instance.recorder_specification is not None: (
        instance.recorder_specification.delete())
    if instance.hydrophone_specification is not None:
        instance.hydrophone_specification.delete()
    if instance.acoustic_detector_specification is not None:
        instance.acoustic_detector_specification.delete()
