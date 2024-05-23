"""Equipment models for metadata app"""
from django.db import models


class EquipmentProvider(models.Model):
    class Meta:
        verbose_name = "Equipment - Provider"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, unique=True)
    contact = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)


class RecorderModel(models.Model):
    class Meta:
        unique_together = [
            ["provider", "name"]
        ]
        verbose_name = "Equipment - Recorder - Model"
        ordering = ["provider", "name"]

    def __str__(self):
        return f"{self.provider.name} - {self.name}"

    provider = models.ForeignKey(to=EquipmentProvider, on_delete=models.CASCADE, related_name="recorder_models")
    name = models.CharField(max_length=255)
    number_of_channels = models.IntegerField(null=True, blank=True)
    """Number of recording channels"""


class Recorder(models.Model):
    """Recorder"""

    class Meta:
        unique_together = [
            ["model", "serial_number"]
        ]
        verbose_name = "Equipment - Recorder"

    def __str__(self):
        return f"{self.model}: {self.serial_number}"

    model = models.ForeignKey(to=RecorderModel, on_delete=models.CASCADE, related_name="recorder_items")
    """Model of the recorder"""
    serial_number = models.CharField(max_length=255)
    """Serial number of the recorder"""


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

    provider = models.ForeignKey(to=EquipmentProvider, on_delete=models.CASCADE, related_name="hydrophone_models")
    name = models.CharField(max_length=255)
    directivity = models.TextField(choices=HydrophoneDirectivity.choices, blank=True, null=True)
    """Directivity of the hydrophone"""

    operating_min_temperature = models.FloatField(null=True, blank=True)
    """Minimal temperature where the hydrophone operates (in degree Celsius)"""
    operating_max_temperature = models.FloatField(null=True, blank=True)
    """Maximal temperature where the hydrophone operates (in degree Celsius)"""

    def operating_temperature(self) -> str:
        """Temperature range where the hydrophone operates (in degree Celsius)"""
        if self.operating_max_temperature is not None and self.operating_min_temperature is not None:
            return f"{self.operating_min_temperature}°C < {self.operating_max_temperature}°C"
        return "-"


class Hydrophone(models.Model):
    """Hydrophone"""

    class Meta:
        unique_together = [
            ["model", "serial_number"]
        ]
        verbose_name = "Equipment - Hydrophone"

    def __str__(self):
        return f"{self.model}: {self.serial_number}"

    model = models.ForeignKey(to=HydrophoneModel, on_delete=models.CASCADE, related_name="hydrophone_items")
    """Model of the hydrophone"""
    serial_number = models.CharField(max_length=255)
    """Serial number of the hydrophone"""

    sensitivity = models.FloatField()
    """Average sensitivity of the hydrophone (dB re 1V/µPa), comprising the pre-amplifier if applicable"""

    min_bandwidth = models.FloatField(null=True, blank=True)
    max_bandwidth = models.FloatField(null=True, blank=True)
    """Interval between the lower limiting frequency and the upper limiting frequency within a more or less flat
     response of the hydrophone, comprising the pre-amplifier if applicable"""

    noise_floor = models.FloatField(null=True, blank=True)
    """Self noise of the hydrophone (dB re 1µPa^2/Hz), comprising the pre-amplifier if applicable"""

    min_dynamic_range = models.FloatField(null=True, blank=True)
    max_dynamic_range = models.FloatField(null=True, blank=True)
    """Range between the lowest level and the highest level which the hydrophone can handle (dB SPL RMS or peak),
     comprising the pre-amplifier if applicable"""

    max_operating_depth = models.FloatField(null=True, blank=True)
    """Maximum depth at which hydrophone operates (in meter)"""

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
