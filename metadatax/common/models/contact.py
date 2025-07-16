from django.db import models

from .institution import Institution


class Contact(models.Model):
    """Contact model"""

    class Meta:
        db_table = "metadatax_common_contact"
        unique_together = ("first_name", "last_name")
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    mail = models.EmailField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)

    current_institutions = models.ManyToManyField(Institution, related_name="contacts")

    @property
    def initial_names(self):
        names = self.first_name.split("-")
        initial_first_name = "-".join([f"{n[0]}." for n in names])
        return f"{self.last_name}, {initial_first_name}"
