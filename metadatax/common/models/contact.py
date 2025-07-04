from django.db import models


class Contact(models.Model):
    """Contact model"""

    class Meta:
        db_table = "metadatax_common_contact"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, unique=True)

    mail = models.EmailField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
