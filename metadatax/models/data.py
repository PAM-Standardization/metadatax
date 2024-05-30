"""Acquisition models for metadata app"""
from django.core.validators import MinValueValidator
from django.db import models

from .acquisition import (
    ChannelConfiguration,
    Accessibility,
)


class FileFormat(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(
        max_length=20,
        help_text="Format of the audio file"
    )


class File(models.Model):
    """Recorder file"""

    class Meta:
        unique_together = [
            ["channel_configuration", "name"]
        ]

    channel_configuration = models.ForeignKey(
        to=ChannelConfiguration, on_delete=models.CASCADE,
        help_text="Channel configuration related to this file"
    )
    name = models.CharField(
        max_length=255,
        help_text="Name of the audio file, with extension."
    )
    format = models.ForeignKey(
        to=FileFormat,
        blank=True, null=True, on_delete=models.SET_NULL,
        help_text="Format of the audio file."
    )

    initial_timestamp = models.DateTimeField(
        null=True, blank=True,
        help_text="Date and time of the audio file start (in UTC).",
        verbose_name="Initial timestamp (UTC)"
    )
    duration = models.IntegerField(
        null=True, blank=True,
        validators=[MinValueValidator(0)],
        help_text="Duration of the audio file (in seconds)."
    )
    sampling_frequency = models.IntegerField(
        help_text="Sampling frequency of the audio file (in Hertz). "
                  "If it is different from the channel sampling frequency, resampling has been performed."
    )

    sample_depth = models.IntegerField(
        null=True, blank=True,
        help_text="Number of quantization bits used to represent each sample (in bits). "
                  "If it is different from the channel sampling frequency, re-quantization has been performed."
    )
    storage_location = models.TextField(
        blank=True, null=True,
        help_text="Description of the path to access the data."
    )
    file_size = models.BigIntegerField(
        null=True, blank=True,
        help_text="Total number of bytes of the audio file (in bytes)."
    )

    accessibility = models.TextField(
        choices=Accessibility.choices,
        blank=True, null=True,
        default=Accessibility.REQUEST,
        help_text="Accessibility level of the data."
                  " If the availability is not sure or non-uniform within the audio file, "
                  "the default value is upon request."
    )
