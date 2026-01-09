"""Acquisition models for metadata app"""
from datetime import timedelta

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Min, ExpressionWrapper, F

from metadatax.data.models import File, AudioProperties, DetectionProperties
from metadatax.equipment.models import Equipment
from metadatax.utils import custom_fields
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
        help_text="Date at which the channel configuration started to record (in UTC).",
        verbose_name="Harvest start date (UTC)",
    )
    harvest_ending_date = custom_fields.DateTimeField(
        null=True,
        blank=True,
        help_text="Date at which the channel configuration finished to record in (in UTC).",
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
        audio_start = AudioProperties.objects.filter(
            id__in=self.files.filter(property_type__model="AudioProperties".lower()).values_list("id", flat=True)
        ).aggregate(start=Min('initial_timestamp'))['start']
        detection_start = DetectionProperties.objects.filter(
            id__in=self.files.filter(property_type__model="DetectionProperties".lower()).values_list("id", flat=True)
        ).aggregate(start=Min('start'))['start']
        if not audio_start:
            return detection_start
        return min(audio_start, detection_start)

    @property
    def recording_end_date(self):
        audio_end = AudioProperties.objects.filter(
            id__in=self.files.filter(property_type__model="AudioProperties".lower()).values_list("id", flat=True)
        ).annotate(
            fake_end=ExpressionWrapper(
                F('initial_timestamp') + timedelta(seconds=1) * F('duration'),
                output_field=models.DateTimeField()
            )
        ).aggregate(end=Min('fake_end'))['end']
        detection_end = DetectionProperties.objects.filter(
            id__in=self.files.filter(property_type__model="DetectionProperties".lower()).values_list("id", flat=True)
        ).aggregate(end=Min('end'))['end']
        if not audio_end:
            return detection_end
        return max(audio_end, detection_end)


class ChannelConfigurationFiles(models.Model):
    class Meta:
        unique_together = ["channel_configuration", "file"]
        db_table = "mx_acquisition_channelconfigurationfiles"

    channel_configuration = models.ForeignKey(
        ChannelConfiguration, on_delete=models.CASCADE
    )
    file = models.ForeignKey(File, on_delete=models.CASCADE)
