from django.db import models
from django.db.models import Q

from metadatax.ontology.models import Label


class AcousticDetectorSpecification(models.Model):
    """Acoustic detector specification model"""

    class Meta:
        db_table = "mx_equipment_acousticdetectorspecification"

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
                f"labels: {', '.join([str(label) for label in self.detected_labels.all()])}"
            )
        return " - ".join(info)

    def __eq__(self, other: "AcousticDetectorSpecification") -> bool:
        # Check detected_labels
        self_labels_not_in_other = self.detected_labels.filter(
            ~Q(id__in=other.detected_labels.values_list("id", flat=True)))
        if self_labels_not_in_other.exists():
            return False
        other_labels_not_in_self = other.detected_labels.filter(
            ~Q(id__in=self.detected_labels.values_list("id", flat=True)))
        if other_labels_not_in_self.exists():
            return False

        return (self.min_frequency == other.min_frequency and
                self.max_frequency == other.max_frequency and
                self.algorithm_name == other.algorithm_name)

    detected_labels = models.ManyToManyField(Label, related_name="acoustic_detectors")

    min_frequency = models.IntegerField(
        blank=True,
        null=True,
        help_text='Minimum frequency of the detections (in Hertz).',
    )
    max_frequency = models.IntegerField(
        blank=True,
        null=True,
        help_text='Maximum frequency of the detections (in Hertz).',
    )
    algorithm_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text='Name of the algorithm used by the detector.',
    )
