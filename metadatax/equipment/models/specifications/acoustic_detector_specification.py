from django.db import models

from metadatax.ontology.models import Label


class AcousticDetectorSpecification(models.Model):
    """Acoustic detector specification model"""

    class Meta:
        db_table = "metadatax_equipment_acousticdetectorspecification"

    def __str__(self):
        info = []
        if self.algorithm_name:
            info.append(self.algorithm_name)
        if self.min_frequency:
            info.append(f">{self.min_frequency}Hz")
        if self.max_frequency:
            info.append(f"<{self.max_frequency}Hz")
        if self.detected_labels.exists():
            info.append(
                f"labels: {', '.join([ str(label) for label in self.detected_labels.all()])}"
            )
        return " - ".join(info)

    detected_labels = models.ManyToManyField(Label, related_name="acoustic_detectors")

    min_frequency = models.IntegerField(blank=True, null=True)
    max_frequency = models.IntegerField(blank=True, null=True)
    algorithm_name = models.CharField(max_length=100, blank=True, null=True)
