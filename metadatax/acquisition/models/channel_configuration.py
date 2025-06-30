"""Acquisition models for metadata app"""
import datetime

import pytz
from django.core.validators import MinValueValidator
from django.db import models

from metadatax.data.models import File
from metadatax.equipment.models import Equipment
from .channel_configuration_detector_specification import (
    ChannelConfigurationDetectorSpecification,
)
from .channel_configuration_recorder_specification import (
    ChannelConfigurationRecorderSpecification,
)
from .deployment import Deployment


class ChannelConfiguration(models.Model):
    """Configuration of a recorded channel for a Hydrophone on a Recorder in a deployment"""

    class Meta:
        ordering = [
            "deployment",
        ]
        db_table = "metadatax_acquisition_channelconfiguration"

    deployment = models.ForeignKey(
        to=Deployment,
        on_delete=models.CASCADE,
        related_name="channel_configurations",
    )

    recorder_specification = models.OneToOneField(
        ChannelConfigurationRecorderSpecification,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    detector_specification = models.OneToOneField(
        ChannelConfigurationDetectorSpecification,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    other_equipments = models.ManyToManyField(Equipment, blank=True)
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
    harvest_starting_date = models.DateTimeField(
        null=True,
        blank=True,
        default=datetime.datetime(2020, 1, 1, 12, 0, 0, tzinfo=pytz.UTC),
        help_text="Harvest start date at which the channel configuration was idle to record (in UTC).",
        verbose_name="Harvest start date (UTC)",
    )
    harvest_ending_date = models.DateTimeField(
        null=True,
        blank=True,
        default=datetime.datetime(2020, 1, 1, 12, 0, 0, tzinfo=pytz.UTC),
        help_text="Harvest stop date at which the channel configuration finished to record in (in UTC).",
        verbose_name="Harvest stop date (UTC)",
    )
    files = models.ManyToManyField(
        File,
        blank=True,
        through="ChannelConfigurationFiles",
        related_name="channel_configurations",
    )
