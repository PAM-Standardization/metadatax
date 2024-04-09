"""Acquisition models for metadata app"""
from django.db import models

from .acquisition import (
    ChannelConfiguration,
    Accessibility,
)


class File(models.Model):
    """Recorder file"""

    channel_configuration = models.ForeignKey(to=ChannelConfiguration, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    initial_timestamp = models.DateTimeField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    storage_location = models.TextField(null=True, blank=True)
    sampling_frequency = models.IntegerField()
    sample_depth = models.IntegerField(null=True, blank=True)
    bit_counts = models.IntegerField(null=True, blank=True)
    format = models.CharField(max_length=20, null=True, blank=True)  # Non-exhaustive select
    accessibility = models.TextField(choices=Accessibility.choices, null=True, blank=True)
