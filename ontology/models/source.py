from django.db import models
from django.db.models import Q, F


class Source(models.Model):
    """Ontology for the source of the sound"""

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="source_cannot_be_self_parent",
                check=~Q(parent_id=F("id")),
            )
        ]

    def __str__(self):
        return self.english_name

    # Mandatory
    english_name = models.CharField(max_length=255, unique=True)

    # Optional
    latin_name = models.CharField(max_length=255, null=True, blank=True)
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
