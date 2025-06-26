from django.core.validators import MinValueValidator
from django.db import models


class AudioProperties(models.Model):

    sampling_frequency = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text="Sampling frequency of the audio file (in Hertz). "
        "If it is different from the channel sampling frequency, resampling has been performed.",
    )
    initial_timestamp = models.DateTimeField(
        help_text="Date and time of the audio file start (in UTC).",
        verbose_name="Initial timestamp (UTC)",
    )
    duration = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text="Duration of the audio file (in seconds).",
    )

    sample_depth = models.IntegerField(
        null=True,
        blank=True,
        help_text="Number of quantization bits used to represent each sample (in bits). "
        "If it is different from the channel sampling frequency, re-quantization has been performed.",
    )
