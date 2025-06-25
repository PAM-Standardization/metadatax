from django.db import models

from metadatax_ontology.models import Label


class AcousticDetectorSpecification(models.Model):
    """Acoustic detector specification model"""

    detected_labels = models.ManyToManyField(Label, related_name='acoustic_detectors')

    min_frequency = models.IntegerField(blank=True, null=True)
    max_frequency = models.IntegerField(blank=True, null=True)
    algorithm_name = models.CharField(max_length=100, blank=True, null=True)
