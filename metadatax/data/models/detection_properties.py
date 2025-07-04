from django.db import models


class DetectionProperties(models.Model):
    class Meta:
        db_table = "metadatax_data_detectionproperties"

    start = models.DateTimeField(
        help_text="Start of the detection file covering (in UTC).",
        verbose_name="Start timestamp (UTC)",
    )
    end = models.DateTimeField(
        help_text="End of the detection file covering (in UTC).",
        verbose_name="End timestamp (UTC)",
    )
