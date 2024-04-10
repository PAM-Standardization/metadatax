"""Equipment models for metadata app"""
from django.db import models


class Recorder(models.Model):
    """Recorder"""

    class Meta:
        unique_together = [
            ["provider", "model", "serial_number"]
        ]

    def __str__(self):
        return self.provider + " " + str(self.model) + " " + str(self.serial_number)

    provider = models.CharField(max_length=255)
    """Recorder manufacturer"""
    model = models.CharField(max_length=255)
    """Model of the recorder"""
    serial_number = models.CharField(max_length=255, blank=True, null=True)
    """Serial number of the recorder"""
    number_of_channels = models.IntegerField(null=True, blank=True)
    """Number of recording channels"""


class HydrophoneDirectivity(models.TextChoices):
    """Hydrophone directivity"""

    OMNI_DIRECTIONAL = ("OMNI", "Omni-directional")
    BI_DIRECTIONAL = ("BI", "Bi-directional")
    UNI_DIRECTIONAL = ("UNI", "Uni-directional")
    CARDIOID = ("CAR", "Cardioid")
    SUPERCARDIOID = ("SCAR", "Supercardioid")


class Hydrophone(models.Model):
    """Hydrophone"""

    class Meta:
        unique_together = [
            ["provider", "model", "serial_number"]
        ]

    def __str__(self):
        return self.provider + " " + str(self.model) + " " + str(self.serial_number)

    provider = models.CharField(max_length=255)
    """Hydrophone manufacturer"""
    model = models.CharField(max_length=255)
    """Model of the hydrophone"""
    serial_number = models.CharField(max_length=255, blank=True, null=True)
    """Serial number of the hydrophone"""

    sensitivity = models.FloatField()
    """Average sensitivity of the hydrophone (dB re 1V/µPa), comprising the pre-amplifier if applicable"""
    directivity = models.TextField(choices=HydrophoneDirectivity.choices, blank=True, null=True)
    """Directivity of the hydrophone"""
    bandwidth = models.FloatField(null=True, blank=True)
    """Interval between the lower limiting frequency and the upper limiting frequency within a more or less flat
     response of the hydrophone, comprising the pre-amplifier if applicable"""
    noise_floor = models.FloatField(null=True, blank=True)
    """Self noise of the hydrophone (dB re 1µPa^2/Hz), comprising the pre-amplifier if applicable"""
    dynamic_range = models.FloatField(null=True, blank=True)
    """Range between the lowest level and the highest level which the hydrophone can handle (dB SPL RMS or peak),
     comprising the pre-amplifier if applicable"""
    max_operating_depth = models.FloatField(null=True, blank=True)
    """Maximum depth at which hydrophone operates (in meter)"""
    operating_min_temperature = models.FloatField(null=True, blank=True)
    """Minimal temperature where the hydrophone operates (in degree Celsius)"""
    operating_max_temperature = models.FloatField(null=True, blank=True)
    """Maximal temperature where the hydrophone operates (in degree Celsius)"""
