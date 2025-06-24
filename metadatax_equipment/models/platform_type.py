from django.db import models


class PlatformType(models.Model):
    """Platform type model"""

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, unique=True)
    is_mobile = models.BooleanField(default=False)
