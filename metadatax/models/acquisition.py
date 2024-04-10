"""Acquisition models for metadata app"""
from django.db import models
from django.db.models import Min, Max, Count

from .equipment import (
    Hydrophone,
    Recorder
)


class Institution(models.Model):
    """Institution"""

    def __str__(self):
        return str(self.name)

    name = models.CharField(max_length=255, unique=True)
    contact = models.TextField(blank=True, null=True)


class Accessibility(models.TextChoices):
    """Accessibility level of the data. Multiple choices are offered : open access, upon request, confidential. """

    CONFIDENTIAL = ("C", "Confidential")
    REQUEST = ("R", "Upon request")
    OPEN = ("O", "Open access")


class Project(models.Model):
    """Data acquisition project"""

    def __str__(self):
        return str(self.name)

    name = models.CharField(max_length=255)
    """Name of the project"""

    responsible_parties = models.ManyToManyField(Institution, related_name="projects")
    """Name of the institutions involved in the data collection and processing"""

    accessibility = models.TextField(choices=Accessibility.choices, blank=True, null=True)

    doi = models.CharField(max_length=255, blank=True, null=True)
    """Digital Object Identifier of the data, if existing"""

    project_type = models.TextField(blank=True, null=True)  # Non-exhaustive select
    """Indicates the type of the project. (research, marine renewable energies, long monitoring).
     Can contain multiple values"""

    project_goal = models.TextField(blank=True, null=True)
    """Goal of the project"""

    def list_responsible_parties(self) -> str:
        """Display readable list of responsible_parties"""
        return ", ".join([p.name for p in self.responsible_parties.all()])


class Deployment(models.Model):
    """Material deployment for data acquisition"""

    def __str__(self):
        return str(self.name)

    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name="deployments")
    provider = models.ForeignKey(to=Institution, on_delete=models.CASCADE, blank=True, null=True)
    """Name company that collected the data"""

    campaign = models.CharField(max_length=255, blank=True, null=True)
    """Name of the campaign during which the deployment was done"""

    name = models.CharField(max_length=255, blank=True, null=True)
    """Name of the deployment (eg deployment 1)"""

    deployment_date = models.DateTimeField(null=True, blank=True)
    """Date and time at which the measurement system was deployed"""
    deployment_vessel = models.CharField(max_length=255, blank=True, null=True)
    """Vessel with which the measurement system was deployed"""

    recovery_date = models.DateTimeField(null=True, blank=True)
    """Date and time at which the measurement system was recovered"""
    recovery_vessel = models.CharField(max_length=255, blank=True, null=True)
    """Vessel with which the measurement system was recovered"""

    description = models.TextField(blank=True, null=True)
    """Optional description of how the deployment and recovery went"""

    platform_type = models.TextField()  # Non-exhaustive select
    """Type of platform, i.e. the support of the measurement systems. 
    Multiple choices are offered : bouy, cage, mooring line with acoustic release, fishing net, glider, whale
    Can contain multiple values"""
    platform_description = models.TextField(blank=True, null=True)
    """Short description of the platform"""
    platform_name = models.CharField(max_length=255, blank=True, null=True)
    """Name of the generic location"""

    longitude = models.FloatField()
    """Longitude where data is collected on the platform"""
    latitude = models.FloatField()
    """Latitude where data is collected on the platform"""
    bathymetric_depth = models.IntegerField(null=True, blank=True)
    """Depth at which data is collected on the platform"""


class ChannelConfiguration(models.Model):
    """Configuration of a recorded channel for a Hydrophone on a Recorder in a deployment"""

    def __str__(self):
        return f"{self.deployment} ({self.recorder} | {self.hydrophone}"

    deployment = models.ForeignKey(to=Deployment, on_delete=models.CASCADE)
    hydrophone = models.ForeignKey(to=Hydrophone, on_delete=models.CASCADE)
    recorder = models.ForeignKey(to=Recorder, on_delete=models.CASCADE)

    channel_name = models.CharField(max_length=5, blank=True, null=True)
    """Name of the channel used for recording"""

    gain = models.IntegerField()
    """Gain of the channel (recorder), with correction factors if applicable, without hydrophone sensibility (in dB). 
    If end-to-end calibration with hydrophone sensibility, set it in Sensitivity and set Gain to 0 dB."""

    hydrophone_depth = models.IntegerField(null=True, blank=True)
    """Depth of hydrophone"""

    continuous = models.BooleanField(null=True, blank=True)
    """Boolean. 1 if the recording is continuous, else 0."""
    duty_cycle_on = models.IntegerField(null=True, blank=True)
    """If Continuous = 0, this value is equal to the time bin during which the recorder in on """
    duty_cycle_off = models.IntegerField(null=True, blank=True)
    """If Continuous = 0, this value is equal to the time bin during which the recorder in off"""

    sampling_frequency = models.IntegerField()
    """Sampling frequency of the recorder"""

    recording_format = models.CharField(max_length=20, blank=True, null=True)  # Non-exhaustive select
    """Format of the audio files (Multiple choices are offered : wav, flac"""
    sample_depth = models.IntegerField()
    """Number of bits per sample"""

    def duty_cycle(self) -> str:
        """Display duty_cycle information"""
        if self.continuous:
            return "Continuous"
        return f"ON: {self.duty_cycle_on} - OFF: {self.duty_cycle_off}"
