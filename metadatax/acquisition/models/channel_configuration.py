"""Acquisition models for metadata app"""
from datetime import timedelta

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Min, ExpressionWrapper, Max, F

from metadatax.data.models import File
from metadatax.equipment.models import Equipment
from metadatax.utils import custom_fields
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

    def __str__(self):
        return f"{self.deployment} [{self.id}]"

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
        help_text="Harvest stop date at which the channel configuration finished to record in (in UTC).",
        verbose_name="Harvest stop date (UTC)",
    )
    files = models.ManyToManyField(
        File,
        blank=True,
        through="ChannelConfigurationFiles",
        related_name="channel_configurations",
    )

    @property
    def recording_start_date(self):
        return self.files.aggregate(start=Min('audio_properties__initial_timestamp'))['start']

    @property
    def recording_end_date(self):
        return self.files.annotate(
            fake_end=ExpressionWrapper(
                F('start') + timedelta(seconds=1) * F('duration'),
                output_field=models.DateTimeField()
            )
        ).aggregate(end=Max('end'))['end']
