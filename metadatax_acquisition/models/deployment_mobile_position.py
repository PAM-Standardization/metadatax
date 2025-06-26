from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import pre_init
from django.dispatch import receiver
from rest_framework.exceptions import ValidationError

from .deployment import Deployment


class DeploymentMobilePosition(models.Model):
    class Meta:
        unique_together = ["deployment", "datetime"]

    deployment = models.ForeignKey(
        to=Deployment,
        on_delete=models.CASCADE,
        help_text="Related deployment",
        related_name="mobile_positions",
    )
    datetime = models.DateTimeField(
        help_text="Datetime for the mobile platform position"
    )
    longitude = models.FloatField(help_text="Longitude of the mobile platform")
    latitude = models.FloatField(help_text="Latitude of the mobile platform")
    depth = models.FloatField(
        help_text="Hydrophone depth of the mobile platform (In positive meters)",
        validators=[
            MinValueValidator(0),
        ],
    )

    heading = models.FloatField(
        null=True, blank=True, default=0.0, help_text="Heading of the mobile platform"
    )
    pitch = models.FloatField(
        null=True, blank=True, default=0.0, help_text="Pitch of the mobile platform"
    )
    roll = models.FloatField(
        null=True, blank=True, default=0.0, help_text="Roll of the mobile platform"
    )


@receiver(pre_init, sender=DeploymentMobilePosition)
def assure_mobile_position_is_on_mobile_deployment(sender, args, signal, **kwargs):
    if not kwargs or not kwargs["kwargs"]:
        return
    deployment: Deployment = kwargs["kwargs"]["deployment"]
    if not deployment.platform or not deployment.platform.type.is_mobile:
        raise ValidationError(
            detail="Deployment mobile position should be on a deployment with a mobile platform",
            code="invalid",
        )
