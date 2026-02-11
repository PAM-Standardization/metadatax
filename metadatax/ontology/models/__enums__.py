from django_extension.models import ExtendedEnum


class SignalShape(ExtendedEnum):
    """Types of signal shapes"""

    STATIONARY = ("S", "Stationary")
    PULSE = ("P", "Pulse")
    FREQUENCY_MODULATION = ("FM", "Frequency modulation")


class SignalPlurality(ExtendedEnum):
    """Plurality of signal(s)"""

    ONE = ("O", "One")
    SET = ("S", "Set")
    REPETITIVE_SET = ("RS", "Repetitive Set")
