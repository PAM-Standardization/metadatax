from django.db import models
from django_extension.models.constraints import NoSelfParentConstraint

from metadatax.bibliography.models import Bibliography
from .__enums__ import LabelDisplay


class Sound(models.Model):
    """Ontology for the sound type"""

    class Meta:
        constraints = [
            NoSelfParentConstraint(
                name="sound_cannot_be_self_parent",
            )
        ]
        db_table = "mx_ontology_sound"
        ordering = ["english_name"]

    def __str__(self):
        return self.english_name

    # Mandatory
    english_name = models.CharField(max_length=255, unique=True)

    # Optional
    french_name = models.CharField(max_length=255, null=True, blank=True)
    code_name = models.CharField(max_length=20, null=True, blank=True)
    taxon = models.CharField(max_length=255, null=True, blank=True)

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.SET_NULL,
    )

    related_bibliography = models.ManyToManyField(
        Bibliography, related_name="related_sounds", blank=True
    )

    def display(self, display: LabelDisplay):
        if display == LabelDisplay.FRENCH and self.french_name:
            return self.french_name
        if display == LabelDisplay.CODE and self.code_name:
            return self.code_name
        return self.english_name
