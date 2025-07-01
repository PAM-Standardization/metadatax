"""Acquisition models for metadata app"""

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from metadatax.data.models import FileFormat
from metadatax.equipment.models import Equipment


def validate_recorder(value: Equipment):
    if value.recorder_specification is None:
        raise ValidationError(
            _("Recorder specification should be linked to a recorder equipment"),
            params={"value": value},
        )


def validate_hydrophone(value: Equipment):
    if value.hydrophone_specification is None:
        raise ValidationError(
            _("Hydrophone specification should be linked to a hydrophone equipment"),
            params={"value": value},
        )


class ChannelConfigurationRecorderSpecification(models.Model):
    class Meta:
        db_table = "metadatax_acquisition_channelconfigurationrecorderspecification"

    recorder = models.ForeignKey(
        Equipment,
        on_delete=models.PROTECT,
        related_name="channel_configuration_recorder_specifications",
        validators=[validate_recorder],
    )
    hydrophone = models.ForeignKey(
        Equipment,
        on_delete=models.PROTECT,
        related_name="channel_configuration_hydrophone_specifications",
        validators=[validate_hydrophone],
    )
    recording_formats = models.ManyToManyField(
        FileFormat, related_name="channel_configuration_recorder_specifications"
    )
    sampling_frequency = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text="Sampling frequency of the recording channel (in Hertz).",
    )
    sample_depth = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text="Number of quantization bits used to represent each sample by the recorder channel (in bits).",
    )
    gain = models.FloatField(
        help_text="Gain of the channel (recorder), with correction factors if applicable, "
        "without hydrophone sensibility (in dB). If end-to-end calibration with hydrophone sensibility, "
        "set it in Sensitivity and set Gain to 0 dB.<br>"
        "Gain G of the channel such that : data(uPa) = data(volt)*10^((-Sh-G)/20). "
        "See Sensitivity for Sh definition."
    )

    channel_name = models.CharField(
        max_length=5,
        blank=True,
        null=True,
        default="A",
        help_text="Name of the channel used for recording.",
    )
