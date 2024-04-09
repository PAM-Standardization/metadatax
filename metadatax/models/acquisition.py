"""Acquisition models for metadata app"""
from django.db import models

from .equipment import (
    Hydrophone,
    Recorder
)


class Institution(models.Model):
    """Institution"""

    def __str__(self):
        return str(self.name)

    name = models.CharField(max_length=255)
    contact = models.TextField(null=True, blank=True)


class Accessibility(models.TextChoices):
    """Data Accessibility"""

    CONFIDENTIAL = ("C", "Confidential")
    REQUEST = ("R", "Upon request")
    OPEN = ("O", "Open access")


class Project(models.Model):
    """Data acquisition project"""

    def __str__(self):
        return str(self.name)

    name = models.CharField(max_length=255)
    responsible_parties = models.ManyToManyField(Institution, related_name="projects")
    accessibility = models.TextField(choices=Accessibility.choices, null=True, blank=True)
    doi = models.CharField(max_length=255, null=True, blank=True)
    project_type = models.TextField(null=True, blank=True)  # Non-exhaustive select
    project_goal = models.TextField(null=True, blank=True)


class Deployment(models.Model):
    """Material deployment for data acquisition"""

    def __str__(self):
        return str(self.name)

    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    provider = models.ForeignKey(to=Institution, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    bathymetric_depth = models.IntegerField(null=True, blank=True)
    deployment_date = models.DateTimeField(null=True, blank=True)
    recovery_date = models.DateTimeField(null=True, blank=True)
    deployment_vessel = models.CharField(max_length=255, null=True, blank=True)
    recovery_vessel = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    campaign = models.CharField(max_length=255, null=True, blank=True)
    platform_name = models.CharField(max_length=255, null=True, blank=True)
    platform_type = models.TextField()  # Non-exhaustive select
    platform_description = models.TextField(null=True, blank=True)


class ChannelConfiguration(models.Model):
    """Configuration of a recorded channel for a Hydrophone on a Recorder in a deployment"""

    deployment = models.ForeignKey(to=Deployment, on_delete=models.CASCADE)
    hydrophone = models.ForeignKey(to=Hydrophone, on_delete=models.CASCADE)
    recorder = models.ForeignKey(to=Recorder, on_delete=models.CASCADE)
    channel_name = models.CharField(max_length=5, null=True, blank=True)
    continuous = models.BooleanField(null=True, blank=True)
    duty_cycle_on = models.IntegerField(null=True, blank=True)
    duty_cycle_off = models.IntegerField(null=True, blank=True)
    sampling_frequency = models.IntegerField()
    gain = models.IntegerField()
    sample_depth = models.IntegerField()
    hydrophone_depth = models.IntegerField(null=True, blank=True)
    recording_format = models.TextField(null=True, blank=True)  # Non-exhaustive select
