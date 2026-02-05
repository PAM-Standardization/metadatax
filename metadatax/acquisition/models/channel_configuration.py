"""Acquisition models for metadata app"""

from django.core.validators import MinValueValidator
from django.db import models

from metadatax.data.models import File
from metadatax.equipment.models import Equipment
from metadatax.utils import custom_fields
from .__enums__ import ChannelConfigurationStatus
from .channel_configuration_specifications import (
    ChannelConfigurationDetectorSpecification,
    ChannelConfigurationRecorderSpecification,
)
from .deployment import Deployment


class ChannelConfiguration(models.Model):
    """Configuration of a recorded channel for a Hydrophone on a Recorder in a deployment"""

    class Meta:
        ordering = [
            "deployment",
        ]
        db_table = "mx_acquisition_channelconfiguration"

    def __str__(self):
        return f"{self.deployment} [{self.id}]"

    deployment = models.ForeignKey(
        to=Deployment,
        on_delete=models.CASCADE,
        related_name="channel_configurations",
    )

    status = models.CharField(
        choices=ChannelConfigurationStatus.choices,
        max_length=1,
        blank=True,
        null=True,
        default=ChannelConfigurationStatus.ACTIVE,
    )

    recorder_specification = models.OneToOneField(
        ChannelConfigurationRecorderSpecification,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="channel_configuration",
        help_text="Each specification is dedicated to one file.",
    )
    detector_specification = models.OneToOneField(
        ChannelConfigurationDetectorSpecification,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="channel_configuration",
        help_text="Each specification is dedicated to one file.",
    )
    storages = models.ManyToManyField(
        Equipment,
        related_name="channel_configurations",
        blank=True,
    )
    continuous = models.BooleanField(
        null=True,
        blank=True,
        help_text="Boolean indicating if the record is continuous (1) or has a duty cycle (0).",
    )
    duty_cycle_on = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
        help_text="If it's not Continuous, time length (in second) during which the recorder is on.",
    )
    duty_cycle_off = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
        help_text="If it's not Continuous, time length (in second) during which the recorder is off.",
    )
    instrument_depth = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
        help_text="Immersion depth of instrument (in positive meters).",
    )
    timezone = models.CharField(max_length=50, null=True, blank=True)
    extra_information = models.TextField(blank=True, null=True)
    harvest_starting_date = custom_fields.DateTimeField(
        null=True,
        blank=True,
        help_text="Harvest start date at which the channel configuration was idle to record (in UTC).",
        verbose_name="Harvest start date (UTC)",
    )
    harvest_ending_date = custom_fields.DateTimeField(
        null=True,
        blank=True,
        help_text="Harvest stop date at which the channel configuration was stopped (in UTC).",
        verbose_name="Harvest stop date (UTC)",
    )
    record_start_date = custom_fields.DateTimeField(
        null=True,
        blank=True,
        help_text="Date at which the channel configuration started to record (in UTC).",
        verbose_name="Record start date (UTC)",
    )
    record_end_date = custom_fields.DateTimeField(
        null=True,
        blank=True,
        help_text="Date at which the channel configuration finished to record in (in UTC).",
        verbose_name="Record stop date (UTC)",
    )
    files = models.ManyToManyField(
        File,
        blank=True,
        through="ChannelConfigurationFiles",
        related_name="channel_configurations",
    )


class ChannelConfigurationFiles(models.Model):
    class Meta:
        unique_together = ["channel_configuration", "file"]
        db_table = "mx_acquisition_channelconfigurationfiles"

    channel_configuration = models.ForeignKey(
        ChannelConfiguration, on_delete=models.CASCADE
    )
    file = models.ForeignKey(File, on_delete=models.CASCADE)
