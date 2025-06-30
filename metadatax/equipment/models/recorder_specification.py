from django.db import models


class RecorderSpecification(models.Model):
    """Recorder Specification model"""

    class Meta:
        db_table = 'metadatax_equipment_recorderspecification'

    channels_count = models.IntegerField(
        blank=True,
        null=True,
        help_text="Number of all the channels on the recorder, even if unused.",
    )
    sd_slots_count = models.IntegerField(blank=True, null=True)
    sd_maximum_capacity = models.IntegerField(blank=True, null=True, help_text="In byte")
    sd_type = models.CharField(max_length=100, blank=True, null=True)
