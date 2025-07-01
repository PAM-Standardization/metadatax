from django.db import models

from metadatax.ontology.models import Label


class AcousticDetectorSpecification(models.Model):
    """Acoustic detector specification model"""

    class Meta:
        db_table = 'metadatax_equipment_acousticdetectorspecification'

    detected_labels = models.ManyToManyField(Label, related_name='acoustic_detectors')

    min_frequency = models.IntegerField(blank=True, null=True)
    max_frequency = models.IntegerField(blank=True, null=True)
    algorithm_name = models.CharField(max_length=100, blank=True, null=True)
