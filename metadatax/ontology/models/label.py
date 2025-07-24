from django.core.validators import MinValueValidator
from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField

from metadatax.bibliography.models import Bibliography
from .physical_descriptor import SignalShape, SignalPlurality
from .sound import Sound
from .source import Source


class Label(models.Model):
    """Ontology label: association of a source and a sound"""

    class Meta:
        db_table = "metadatax_ontology_label"
        unique_together = ("source", "sound", "nickname")
        ordering = ("source", "sound", "nickname")

    def __str__(self):
        if self.nickname:
            return self.nickname
        return f"{self.source} - {self.sound}"

    # Mandatory
    source = models.ForeignKey(Source, on_delete=models.PROTECT, related_name="labels")

    # Optional
    sound = models.ForeignKey(
        Sound, on_delete=models.PROTECT, null=True, blank=True, related_name="labels"
    )
    nickname = models.CharField(max_length=255, null=True, blank=True)

    associated_names = ArrayField(
        models.CharField(max_length=255, blank=True, null=True),
        help_text="Other name found in the bibliography for this label",
        null=True,
        blank=True,
    )
    related_bibliography = models.ManyToManyField(
        Bibliography, related_name="related_labels", blank=True
    )

    # Optional
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.SET_NULL,
    )
    shape = models.TextField(
        choices=SignalShape.choices, max_length=2, null=True, blank=True
    )
    plurality = models.TextField(
        choices=SignalPlurality.choices, max_length=2, null=True, blank=True
    )
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
