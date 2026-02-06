"""Acquisition models for metadata app"""

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from metadatax.data.models import FileFormat
from metadatax.equipment.models import Equipment
from metadatax.ontology.models import Label


def validate_detector(value: int):
    equipment = Equipment.objects.get(id=value)
    if not equipment.model.specification_relations.filter(
            specification_type__model="AcousticDetectorSpecification").exists():
        raise ValidationError(
            _("The selected equipment doesn't have acoustic detector specification"),
            params={"equipment": equipment},
        )


class ChannelConfigurationDetectorSpecification(models.Model):
    class Meta:
        db_table = "mx_acquisition_channelconfigurationdetectorspecification"

    def __str__(self):
        info = [
            str(self.detector),
            f"({', '.join([str(f) for f in self.output_formats.all()])})",
            f"({', '.join([str(l) for l in self.labels.all()])})",
        ]
        if self.min_frequency:
            info.append(f">{self.min_frequency}Hz")
        if self.max_frequency:
            info.append(f"<{self.max_frequency}Hz")
        if self.filter:
            info.append("filtered")
        return " - ".join(info)

    detector = models.ForeignKey(
        Equipment,
        on_delete=models.PROTECT,
        related_name="channel_configuration_detector_specifications",
        validators=[validate_detector],
    )
    output_formats = models.ManyToManyField(
        FileFormat, related_name="channel_configuration_detector_specifications"
    )
    labels = models.ManyToManyField(
        Label,
        related_name="channel_configuration_detector_specifications",
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
    filter = models.TextField(
        blank=True,
        null=True,
        help_text='Filter applied to the configuration',
    )
    configuration = models.TextField(
        blank=True,
        null=True,
        help_text='Description of the configuration',
    )
