from django.db import models

from .sound import Sound
from .source import Source


class Label(models.Model):
    """Ontology label: association of a source and a sound"""

    class Meta:
        db_table = "metadatax_ontology_label"

    def __str__(self):
        return f"{self.source} - {self.sound}"

    # Mandatory
    source = models.ForeignKey(Source, on_delete=models.PROTECT, related_name="labels")

    # Optional
    sound = models.ForeignKey(
        Sound, on_delete=models.PROTECT, null=True, blank=True, related_name="labels"
    )
    nickname = models.CharField(max_length=255, null=True, blank=True)
