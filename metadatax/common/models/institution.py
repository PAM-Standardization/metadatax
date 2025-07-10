from django.db import models


class Institution(models.Model):
    """Scientist institution model"""

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, unique=True)

    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    mail = models.EmailField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)

    @property
    def location(self):
        return f"{self.city}, {self.country}"
