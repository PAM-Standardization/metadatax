from django.db import models


class Behavior(models.Model):
    """Ontology for a source behavior"""

    class Meta:
        db_table = "mx_ontology_behavior"
        ordering = ["name"]

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, unique=True)
