"""Equipment models for metadata app"""
from django.core.validators import MinValueValidator
from django.db import models


class EquipmentProvider(models.Model):
    class Meta:
        verbose_name = "Equipment - Provider"
        ordering = ["name"]

    def __str__(self):
        return self.name

    name = models.CharField(
        max_length=255,
        unique=True,
        help_text="Name of the manufacturer"
    )
    contact = models.EmailField(
        blank=True, null=True,
        help_text="Contact email of the manufacturer"
    )
    website = models.URLField(
        blank=True, null=True,
        help_text="Website of the manufacturer"
    )


class RecorderModel(models.Model):
    class Meta:
        unique_together = [
            ["provider", "name"]
        ]
        verbose_name = "Equipment - Recorder - Model"
        ordering = ["provider", "name"]

    def __str__(self):
        return f"{self.provider.name} - {self.name}"

    provider = models.ForeignKey(
        to=EquipmentProvider, related_name="recorder_models",
        on_delete=models.CASCADE,
        help_text="Recorder manufacturer."
    )
    name = models.CharField(
        max_length=255,
        help_text="Name of the recorder model."
    )
    number_of_channels = models.IntegerField(
        null=True, blank=True,
        help_text="Number of all the channels on the recorder, even if unused."
    )


class Recorder(models.Model):
    """Recorder"""

    class Meta:
        unique_together = [
            ["model", "serial_number"]
        ]
        verbose_name = "Equipment - Recorder"
        ordering = ["model"]

    def __str__(self):
        return f"{self.model}: {self.serial_number}"

    model = models.ForeignKey(
        to=RecorderModel, related_name="recorder_items",
        on_delete=models.CASCADE,
        help_text="Model of the recorder"
    )
    serial_number = models.CharField(
        max_length=255,
        help_text="Serial number of the recorder"
    )


class HydrophoneDirectivity(models.TextChoices):
    """Hydrophone directivity"""

    OMNI_DIRECTIONAL = ("OMNI", "Omni-directional")
    BI_DIRECTIONAL = ("BI", "Bi-directional")
    UNI_DIRECTIONAL = ("UNI", "Uni-directional")
    CARDIOID = ("CAR", "Cardioid")
    SUPERCARDIOID = ("SCAR", "Supercardioid")


class HydrophoneModel(models.Model):
    class Meta:
        unique_together = [
            ["provider", "name"]
        ]
        verbose_name = "Equipment - Hydrophone - Model"
        ordering = ["provider", "name"]

    def __str__(self):
        return f"{self.provider.name} - {self.name}"

    provider = models.ForeignKey(
        to=EquipmentProvider, related_name="hydrophone_models",
        on_delete=models.CASCADE,
        help_text="Hydrophone manufacturer."
    )
    name = models.CharField(
        max_length=255,
        help_text="Name of the hydrophone model."
    )
    directivity = models.TextField(
        choices=HydrophoneDirectivity.choices,
        blank=True, null=True,
        help_text="Directivity of the hydrophone"
    )

    operating_min_temperature = models.FloatField(
        null=True, blank=True,
        help_text="Minimal temperature where the hydrophone operates (in degree Celsius)"
    )
    operating_max_temperature = models.FloatField(
        null=True, blank=True,
        help_text="Maximal temperature where the hydrophone operates (in degree Celsius)"
    )
    min_bandwidth = models.FloatField(
        null=True, blank=True,
        help_text="Lower limiting frequency for a more or less flat response of the hydrophone, "
                  "pre-amplification included if applicable."
    )
    max_bandwidth = models.FloatField(
        null=True, blank=True,
        help_text="Upper limiting frequency within a more or less flat response of the hydrophone, "
                  "pre-amplification included if applicable."
    )

    noise_floor = models.FloatField(
        null=True, blank=True,
        help_text="Self noise of the hydrophone (dB re 1µPa^2/Hz), pre-amplification included if applicable.<br>"
                  "Average on bandwidth or a fix frequency (generally @5kHz for example). "
                  "Possibility to 'below sea-state zero' (equivalent to around 30dB @5kHz) could be nice "
                  "because it is often described like that."
    )

    min_dynamic_range = models.FloatField(
        null=True, blank=True,
        help_text="Lowest level which the hydrophone can handle (dB SPL RMS or peak), "
                  "pre-amplification included if applicable."
    )
    max_dynamic_range = models.FloatField(
        null=True, blank=True,
        help_text="Highest level which the hydrophone can handle (dB SPL RMS or peak), "
                  "pre-amplification included if applicable."
    )

    max_operating_depth = models.FloatField(
        null=True, blank=True,
        validators=[MinValueValidator(0)],
        help_text="Maximum depth at which hydrophone operates (in positive meters)."
    )

    def operating_temperature(self) -> str:
        """Temperature range where the hydrophone operates (in degree Celsius)"""
        if self.operating_max_temperature is not None and self.operating_min_temperature is not None:
            return f"{self.operating_min_temperature}°C < {self.operating_max_temperature}°C"
        return "-"

    def bandwidth(self) -> str:
        """Interval between the lower limiting frequency and the upper limiting frequency within a more or less flat
         response of the hydrophone, comprising the pre-amplifier if applicable"""
        if self.min_bandwidth is not None and self.max_bandwidth is not None:
            return f"{self.min_bandwidth}Hz < {self.max_bandwidth}Hz"
        return "-"

    def dynamic_range(self) -> str:
        """Range between the lowest level and the highest level which the hydrophone can handle (dB SPL RMS or peak),
         comprising the pre-amplifier if applicable"""
        if self.min_dynamic_range is not None and self.max_dynamic_range is not None:
            return f"{self.min_dynamic_range} < {self.max_dynamic_range}"
        return "-"


class Hydrophone(models.Model):
    """Hydrophone"""

    class Meta:
        unique_together = [
            ["model", "serial_number"]
        ]
        verbose_name = "Equipment - Hydrophone"
        ordering = ["model"]

    def __str__(self):
        return f"{self.model}: {self.serial_number}"

    model = models.ForeignKey(
        to=HydrophoneModel, related_name="hydrophone_items",
        on_delete=models.CASCADE,
        help_text="Model of the hydrophone"
    )
    serial_number = models.CharField(
        max_length=255,
        help_text="Serial number of the hydrophone"
    )

    sensitivity = models.FloatField(
        help_text="Average sensitivity of the hydrophone (dB re 1V/µPa), pre-amplification included if applicable. "
                  "Sensitivity Sh of the hydrophone such that : data(uPa) = data(volt)*10^((-Sh-G)/20). "
                  "See Recorder Gain for definition of G."
    )
