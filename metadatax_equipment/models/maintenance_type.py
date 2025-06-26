from django.db import models


class MaintenanceType(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, unique=True)

    description = models.TextField(blank=True, null=True)
    interval = models.DurationField(blank=True, null=True)
