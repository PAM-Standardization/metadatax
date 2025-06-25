"""Acquisition models for metadata app"""

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from metadatax_data.models import FileFormat
from metadatax_equipment.models import Equipment
from metadatax_ontology.models import Label


def validate_detector(value: Equipment):
    if value.acoustic_detector_specification is None:
        raise ValidationError(
            _("Detector specification should be linked to a detector equipment"),
            params={"value": value},
        )


class ChannelConfigurationDetectorSpecification(models.Model):
    detector = models.ForeignKey(
        Equipment,
        on_delete=models.PROTECT,
        related_name="channel_configuration_detector_specifications",
        validators=[validate_detector],
    )
    output_formats = models.ManyToManyField(FileFormat)
    labels = models.ManyToManyField(
        Label
    )  # TODO: check labels are in detector detected labels

    min_frequency = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text="Minimum frequency (in Hertz).",
        null=True,
        blank=True,
    )
    max_frequency = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text="Maximum frequency (in Hertz).",
        null=True,
        blank=True,
    )
    filter = models.TextField(blank=True, null=True)
    configuration = models.TextField(blank=True, null=True)
