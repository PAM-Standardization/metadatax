from django.db import models


class SDCardSpecification(models.Model):
    """SD Card Specification model"""

    class Meta:
        db_table = 'metadatax_equipment_sdcardspecification'

    capacity = models.IntegerField(help_text="in byte")
