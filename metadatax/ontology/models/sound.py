from django.db import models
from django.db.models import Q, F

from metadatax.bibliography.models import Bibliography


class Sound(models.Model):
    """Ontology for the sound type"""

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="sound_cannot_be_self_parent",
                check=~Q(parent_id=F("id")),
            )
        ]
        db_table = "metadatax_ontology_sound"

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

    associated_names = models.ManyToManyField("self", related_name="associated_names")
    related_bibliography = models.ManyToManyField(
        Bibliography, related_name="related_sounds"
    )
