from django.db import models


class SignalShape(models.TextChoices):
    """Types of signal shapes"""

    STATIONARY = ("S", "Stationary")
    PULSE = ("P", "Pulse")
    FREQUENCY_MODULATION = ("FM", "Frequency modulation")


class SignalPlurality(models.TextChoices):
    """Plurality of signal(s)"""

    ONE = ("O", "One")
    SET = ("S", "Set")
    REPETITIVE_SET = ("RS", "Repetitive Set")
