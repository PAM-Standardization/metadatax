from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from metadatax.common.models import ContactRole
from metadatax.equipment.models import Platform
from metadatax.utils import custom_fields
from .campaign import Campaign
from .project import Project
from .site import Site


class Deployment(models.Model):
    """Material deployment for data acquisition"""

    class Meta:
        unique_together = ["project", "name", "site", "campaign"]
        ordering = ["project", "name"]
        db_table = "metadatax_acquisition_deployment"

    def __str__(self):
        if self.name is not None:
            return f"{self.project}: {self.name}"
        else:
            return f"{self.project}: {self.campaign.name if self.campaign else '-'} | {self.site.name if self.site else '-'}"

    project = models.ForeignKey(
        to=Project,
        related_name="deployments",
        on_delete=models.CASCADE,
        help_text="Project associated to this deployment",
    )
    longitude = models.FloatField(
        help_text="Longitude of the platform position (WGS84 decimal degree).",
    )
    latitude = models.FloatField(
        help_text="Latitude of the platform position (WGS84 decimal degrees).",
    )

    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Name of the deployment.",
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
    campaign = models.ForeignKey(
        to=Campaign,
        related_name="deployments",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Campaign during which the instrument was deployed.",
    )
    platform = models.ForeignKey(
        to=Platform,
        related_name="deployments",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Support of the deployed instruments",
    )
    bathymetric_depth = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
        help_text="Underwater depth of ocean floor at the platform position (in positive meters).",
    )
    deployment_date = custom_fields.DateTimeField(
        null=True,
        blank=True,
        help_text="Date and time at which the measurement system was deployed in UTC.",
        verbose_name="Deployment date (UTC)",
    )
    deployment_vessel = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Name of the vehicle associated with the deployment.",
    )
    recovery_date = custom_fields.DateTimeField(
        null=True,
        blank=True,
        help_text="Date and time at which the measurement system was recovered in UTC.",
        verbose_name="Recovery date (UTC)",
    )
    recovery_vessel = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Name of the vehicle associated with the recovery.",
    )
    contacts = models.ManyToManyField(
        to=ContactRole,
        related_name="deployments",
        blank=True,
        help_text="Contacts related to the deployment.",
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Optional description of deployment and recovery conditions (weather, technical issues,...).",
    )

    def clean(self):
        if self.campaign and self.campaign.project != self.project:
            raise ValidationError("Campaign must belong to the Deployment project")
        if self.site and self.site.project != self.project:
            raise ValidationError("Site must belong to the Deployment project")
        if self.name is None and self.site is None and self.campaign is None:
            raise ValidationError(
                "Your deployment must be identified by either a name, campaign and/or site"
            )
