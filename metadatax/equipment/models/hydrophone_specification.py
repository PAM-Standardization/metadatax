from django.core.validators import MinValueValidator
from django.db import models

from .hydrophone_directivity import HydrophoneDirectivity


class HydrophoneSpecification(models.Model):
    """Hydrophone Specification model"""

    class Meta:
        db_table = 'metadatax_equipment_hydrophonespecification'

    sensitivity = models.FloatField()

    directivity = models.TextField(
        choices=HydrophoneDirectivity.choices,
        blank=True,
        null=True,
        help_text="Directivity of the hydrophone",
    )
    operating_min_temperature = models.FloatField(
        null=True,
        blank=True,
        help_text="Minimal temperature where the hydrophone operates (in degree Celsius)",
    )
    operating_max_temperature = models.FloatField(
        null=True,
        blank=True,
        help_text="Maximal temperature where the hydrophone operates (in degree Celsius)",
    )
    min_bandwidth = models.FloatField(
        null=True,
        blank=True,
        help_text="Lower limiting frequency for a more or less flat response of the hydrophone, "
                  "pre-amplification included if applicable.",
    )
    max_bandwidth = models.FloatField(
        null=True,
        blank=True,
        help_text="Upper limiting frequency within a more or less flat response of the hydrophone, "
                  "pre-amplification included if applicable.",
    )
    min_dynamic_range = models.FloatField(
        null=True,
        blank=True,
        help_text="Lowest level which the hydrophone can handle (dB SPL RMS or peak), "
                  "pre-amplification included if applicable.",
    )
    max_dynamic_range = models.FloatField(
        null=True,
        blank=True,
        help_text="Highest level which the hydrophone can handle (dB SPL RMS or peak), "
                  "pre-amplification included if applicable.",
    )
    min_operating_depth = models.FloatField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
        help_text="Minimum depth at which hydrophone operates (in positive meters).",
    )
    max_operating_depth = models.FloatField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
        help_text="Maximum depth at which hydrophone operates (in positive meters).",
    )
    noise_floor = models.FloatField(
        null=True,
        blank=True,
        help_text="Self noise of the hydrophone (dB re 1µPa^2/Hz), pre-amplification included if applicable.<br>"
                  "Average on bandwidth or a fix frequency (generally @5kHz for example). "
                  "Possibility to 'below sea-state zero' (equivalent to around 30dB @5kHz) could be nice "
                  "because it is often described like that.",
    )
