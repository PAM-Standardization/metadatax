"""Acquisition models for metadata app"""
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.safestring import mark_safe

from .equipment import Hydrophone, Recorder
import datetime


class Institution(models.Model):
    """Institution"""

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return str(self.name)

    name = models.CharField(
        max_length=255,
        unique=True,
        help_text=mark_safe(
            "Name of the institutions involved in the data collection and processing. "
            "It is based on the SeaDataNet list "
            '(<a href="https://edmo.seadatanet.org/search" target="_blank">https://edmo.seadatanet.org/search</a>),'
            " but an unlisted institution can be added if required."
        ),
    )
    contact = models.EmailField(help_text="Generic and permanent email address")
    website = models.URLField(
        blank=True, null=True, help_text="If exists, the website URL of the institution"
    )


class Accessibility(models.TextChoices):
    """Accessibility level of the data. Multiple choices are offered : open access, upon request, confidential."""

    CONFIDENTIAL = ("C", "Confidential")
    REQUEST = ("R", "Upon request")
    OPEN = ("O", "Open access")


class ProjectType(models.Model):
    """Indicates the type of the project. (research, marine renewable energies, long monitoring).
    Can contain multiple values"""

    class Meta:
        verbose_name = "Project - Type"
        ordering = ["name"]

    def __str__(self):
        return str(self.name)

    name = models.CharField(
        max_length=255, unique=True, help_text="Description of the type of the project"
    )


class Project(models.Model):
    """Data acquisition project"""

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return str(self.name)

    name = models.CharField(max_length=255, help_text="Name of the project")

    responsible_parties = models.ManyToManyField(
        Institution,
        related_name="projects",
        help_text="Name of the institutions involved in the data collection and processing within the project.",
    )

    accessibility = models.TextField(
        choices=Accessibility.choices,
        blank=True,
        null=True,
        default=Accessibility.REQUEST,
        help_text="Accessibility level of the data. If the availability is not sure or non-uniform within the project, "
        "the default value is upon request.",
    )

    doi = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Digital Object Identifier of the data, if existing.",
    )

    project_type = models.ForeignKey(
        to=ProjectType,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="projects",
        help_text="Description of the type of the project "
        "(e.g., research, marine renewable energies, long monitoring,...).",
    )

    project_goal = models.TextField(
        blank=True, null=True, help_text="Description of the goal of the project."
    )


class Campaign(models.Model):
    """Name of the campaign during which the deployment was done"""

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name="unique_campaign_in_project",
                fields=["name", "project_id"],
            ),
        ]
        verbose_name = "Project - Campaign"
        ordering = ["project", "name"]

    def __str__(self):
        return self.project.name + " " + str(self.name)

    name = models.CharField(
        max_length=255,
        help_text="Name of the campaign during which the instrument was deployed.",
    )
    project = models.ForeignKey(
        to=Project,
        related_name="campaigns",
        on_delete=models.CASCADE,
        help_text="Project associated to this campaign",
    )


class Site(models.Model):
    """Name of the site where the deployment was done"""

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name="unique_site_in_project",
                fields=["name", "project_id"],
            ),
        ]
        verbose_name = "Project - Site"
        ordering = ["project", "name"]

    def __str__(self):
        return self.project.name + " " + str(self.name)

    name = models.CharField(
        max_length=255,
        help_text="Name of the platform conceptual location. "
        "A site may group together several platforms in relatively close proximity, "
        "or describes a location where regular deployments are carried out.",
    )
    """Name of the generic location"""
    project = models.ForeignKey(
        to=Project,
        related_name="sites",
        on_delete=models.CASCADE,
        help_text="Project associated to this site",
    )


class PlatformType(models.Model):
    class Meta:
        verbose_name = "Deployment - Platform - Type"
        ordering = ["name"]

    def __str__(self):
        return str(self.name)

    name = models.CharField(
        max_length=255,
        unique=True,
        help_text="Generic name of the support of the deployed instruments",
    )


class Platform(models.Model):
    class Meta:
        verbose_name = "Deployment - Platform"
        ordering = ["name"]

    def __str__(self):
        if self.name:
            return str(self.name)
        return f"{self.type}[{self.id}]"

    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Name of the specific support of the deployed instruments",
    )
    type = models.ForeignKey(
        to=PlatformType,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="platforms",
        help_text="Generic type of support",
    )
    description = models.TextField(
        blank=True, null=True, help_text="Optional description of the platform."
    )


class Deployment(models.Model):
    """Material deployment for data acquisition"""

    class Meta:
        ordering = ["project", "name"]

    def __str__(self):
        if self.name is not None:
            return str(self.name)
        else:
            return f"{self.project}: {self.campaign.name if self.campaign else '-'} | {self.site.name if self.site else '-'}"

    def clean(self):
        if self.campaign and self.campaign.project != self.project:
            raise ValidationError("Campaign must belong to the Deployment project")
        if self.site and self.site.project != self.project:
            raise ValidationError("Site must belong to the Deployment project")
        if self.name is None and self.site is None and self.campaign is None:
            raise ValidationError(
                "Your deployment must be identified by either a name, campaign and/or site"
            )

    name = models.CharField(
        max_length=255, blank=True, null=True, help_text="Name of the deployment."
    )

    project = models.ForeignKey(
        to=Project,
        related_name="deployments",
        on_delete=models.CASCADE,
        help_text="Project associated to this deployment",
    )
    provider = models.ForeignKey(
        to=Institution,
        related_name="deployments",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Name of the institution that deployed the instrument and collected the data.",
    )

    campaign = models.ForeignKey(
        to=Campaign,
        related_name="deployments",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Campaign during which the instrument was deployed.",
    )

    site = models.ForeignKey(
        to=Site,
        related_name="deployments",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Conceptual location. "
        "A site may group together several platforms in relatively close proximity, "
        "or describes a location where regular deployments are carried out.",
    )

    platform = models.ForeignKey(
        to=Platform,
        related_name="deployments",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Support of the deployed instruments",
    )

    deployment_date = models.DateTimeField(
        null=True,
        blank=True,
        default=datetime.datetime(2020, 1, 1, 12, 0, 0),
        help_text="Date and time at which the measurement system was deployed in UTC.",
        verbose_name="Deployment date (UTC)",
    )

    deployment_vessel = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Name of the vehicle associated with the deployment.",
    )

    recovery_date = models.DateTimeField(
        null=True,
        blank=True,
        default=datetime.datetime(2020, 1, 1, 12, 0, 0),
        help_text="Date and time at which the measurement system was recovered in UTC.",
        verbose_name="Recovery date (UTC)",
    )
    recovery_vessel = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Name of the vehicle associated with the recovery.",
    )

    description = models.TextField(
        blank=True,
        null=True,
        help_text="Optional description of deployment and recovery conditions (weather, technical issues,...).",
    )

    longitude = models.FloatField(
        blank=True,
        null=True,
        help_text="Longitude of the platform position (WGS84 decimal degree)."
    )
    latitude = models.FloatField(
        blank=True,
        null=True,
        help_text="Latitude of the platform position (WGS84 decimal degrees)."
    )
    bathymetric_depth = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
        help_text="Underwater depth of ocean floor at the platform position (in positive meters).",
    )

    objects = models.Manager


class ChannelConfiguration(models.Model):
    """Configuration of a recorded channel for a Hydrophone on a Recorder in a deployment"""

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name="unique_name_in_deployment_with_recorder",
                fields=["channel_name", "deployment_id", "recorder_id"],
            ),
        ]
        ordering = ["deployment", "channel_name"]

    def __str__(self):
        return (
            f"{self.deployment} ({self.recorder.model.provider} {self.recorder.model.name} &"
            f" {self.hydrophone.model.provider} {self.hydrophone.model.name})"
        )

    deployment = models.ForeignKey(to=Deployment, on_delete=models.CASCADE)
    hydrophone = models.ForeignKey(to=Hydrophone, on_delete=models.CASCADE)
    recorder = models.ForeignKey(to=Recorder, on_delete=models.CASCADE)

    channel_name = models.CharField(
        max_length=5,
        blank=True,
        null=True,
        default="A",
        help_text="Name of the channel used for recording.",
    )

    gain = models.FloatField(
        help_text="Gain of the channel (recorder), with correction factors if applicable, "
        "without hydrophone sensibility (in dB). If end-to-end calibration with hydrophone sensibility, "
        "set it in Sensitivity and set Gain to 0 dB.<br>"
        "Gain G of the channel such that : data(uPa) = data(volt)*10^((-Sh-G)/20). "
        "See Sensitivity for Sh definition."
    )

    hydrophone_depth = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
        help_text="Immersion depth of hydrophone (in positive meters).",
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

    sampling_frequency = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text="Sampling frequency of the recording channel (in Hertz).",
    )

    recording_format = models.ForeignKey(
        to="FileFormat",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="Format of the recorded files",
    )
    sample_depth = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text="Number of quantization bits used to represent each sample by the recorder channel (in bits).",
    )

    def duty_cycle(self) -> str:
        """Display duty_cycle information"""
        if self.continuous:
            return "Continuous"
        return f"ON: {self.duty_cycle_on} - OFF: {self.duty_cycle_off}"

class MobilePlatform(models.Model):
    deployment = models.ForeignKey(to=Deployment, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    hydrophone_depth = models.FloatField()
    heading = models.FloatField(null=True,
                                blank=True,
                                default=0.0)
    pitch = models.FloatField(null=True,
                              blank=True,
                              default=0.0)
    roll = models.FloatField(null=True,
                             blank=True,
                             default=0.0)
