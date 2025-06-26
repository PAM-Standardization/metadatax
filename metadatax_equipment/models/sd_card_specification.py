from django.db import models


class SDCardSpecification(models.Model):
    """SD Card Specification model"""

    capacity = models.IntegerField(help_text="in byte")
