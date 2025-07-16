from django.core.validators import MinValueValidator
from django.db import models

from metadatax.bibliography.models import Bibliography
from .label import Label


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


class PhysicalDescriptor(models.Model):
    """Physical descriptor of the signal"""

    class Meta:
        db_table = "metadatax_ontology_physicaldescriptor"

    # Mandatory
    shape = models.TextField(choices=SignalShape.choices, max_length=2)
    plurality = models.TextField(choices=SignalPlurality.choices, max_length=2)
    label = models.OneToOneField(
        Label, on_delete=models.CASCADE, related_name="physical_descriptor"
    )

    # Optional
    min_frequency = models.PositiveIntegerField(null=True, blank=True)
    max_frequency = models.PositiveIntegerField(null=True, blank=True)
    mean_duration = models.FloatField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
        ],
    )
    description = models.TextField(null=True, blank=True)

    related_bibliography = models.ManyToManyField(
        Bibliography, related_name="related_physical_descriptors", blank=True
    )
