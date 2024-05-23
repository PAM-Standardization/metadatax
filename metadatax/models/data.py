"""Acquisition models for metadata app"""
from django.db import models

from .acquisition import (
    ChannelConfiguration,
    Accessibility,
)


class FileFormat(models.Model):

    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=20)


class File(models.Model):
    """Recorder file"""

    class Meta:
        unique_together = [
            ["channel_configuration", "name"]
        ]

    channel_configuration = models.ForeignKey(to=ChannelConfiguration, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    """Name of the audio file"""
    format = models.ForeignKey(to=FileFormat, blank=True, null=True, on_delete=models.SET_NULL)
    """Format of the audio file. Audio files can be stored in a different format from the recording format."""

    initial_timestamp = models.DateTimeField(null=True, blank=True)
    """Date and time at the start of the audio file"""
    duration = models.IntegerField(null=True, blank=True)
    """Duration of the audio file (in second)"""
    sampling_frequency = models.IntegerField()
    """Sampling of the audio file (in Hertz)."""

    sample_depth = models.IntegerField(null=True, blank=True)
    """Number of bits per sample (in bits)"""
    storage_location = models.TextField(blank=True, null=True)
    """Path of the folder containing the audio file"""
    bit_counts = models.BigIntegerField(null=True, blank=True)
    """Total number of bits of the audio file"""

    accessibility = models.TextField(choices=Accessibility.choices, blank=True, null=True)
