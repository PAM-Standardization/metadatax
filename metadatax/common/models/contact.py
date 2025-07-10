from django.db import models

from .institution import Institution


class Contact(models.Model):
    """Contact model"""

    class Meta:
        db_table = "metadatax_common_contact"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    mail = models.EmailField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)

    current_institutions = models.ManyToManyField(Institution, related_name="contacts")

    @property
    def initial_names(self):
        names = self.first_name.split("-")
        initial_first_name = "-".join([n[0] for n in names])
        return f"{initial_first_name} {self.last_name}"
