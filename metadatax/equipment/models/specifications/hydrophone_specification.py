from django.core.validators import MinValueValidator
from django.db import models

from .hydrophone_directivity import HydrophoneDirectivity


class HydrophoneSpecification(models.Model):
    """Hydrophone Specification model"""

    class Meta:
        db_table = "metadatax_equipment_hydrophonespecification"
        unique_together = (
            "directivity",
            "operating_min_temperature",
            "operating_max_temperature",
            "min_bandwidth",
            "max_bandwidth",
            "min_dynamic_range",
            "max_dynamic_range",
            "min_operating_depth",
            "max_operating_depth",
            "noise_floor",
        )

    def __str__(self):
        info = []
        optional_info = []
        if self.directivity:
            optional_info.append(self.directivity)
        if self.operating_min_temperature:
            optional_info.append(f">{self.operating_min_temperature}°C")
        if self.operating_max_temperature:
            optional_info.append(f"<{self.operating_max_temperature}°C")
        if self.min_bandwidth:
            optional_info.append(f">{self.min_bandwidth}Hz")
        if self.max_bandwidth:
            optional_info.append(f"<{self.max_bandwidth}Hz")
        if self.min_dynamic_range:
            optional_info.append(f">{self.min_dynamic_range}dB")
        if self.max_dynamic_range:
            optional_info.append(f"<{self.max_dynamic_range}dB")
        if self.min_operating_depth:
            optional_info.append(f">{self.min_operating_depth}m")
        if self.max_operating_depth:
            optional_info.append(f"<{self.max_operating_depth}m")
        if self.noise_floor:
            optional_info.append(f"noise: {self.noise_floor}dB")
        if len(optional_info) > 0:
            info.append(f"({', '.join(optional_info)})")
        return ", ".join(info)

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
