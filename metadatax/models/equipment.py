"""Equipment models for metadata app"""
from django.db import models


class Recorder(models.Model):
    """Recorder"""

    provider = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255, null=True, blank=True)
    number_of_channels = models.IntegerField(null=True, blank=True)


class HydrophoneDirectivity(models.TextChoices):
    """Hydrophone directivity"""

    OMNIDIRECTIONAL = ("OMNI", "Omni-directional")
    BIDIRECTIONAL = ("BI", "Bi-directional")
    UNIDIRECTIONAL = ("UNI", "Uni-directional")


class Hydrophone(models.Model):
    """Hydrophone"""

    provider = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255, null=True, blank=True)
    sensitivity = models.FloatField()
    directivity = models.TextField(choices=HydrophoneDirectivity.choices, null=True, blank=True)
    bandwidth = models.FloatField(null=True, blank=True)
    noise_floor = models.FloatField(null=True, blank=True)
    dynamic_range = models.FloatField(null=True, blank=True)
