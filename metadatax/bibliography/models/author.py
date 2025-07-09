from django.db import models

from metadatax.common.models import Contact, Institution
from .bibliography import Bibliography


class Author(models.Model):
    class Meta:
        unique_together = (("order", "bibliography"),)

    def __str__(self):
        return f"{self.order} {self.contact}"

    order = models.PositiveIntegerField()
    bibliography = models.ForeignKey(
        to=Bibliography,
        on_delete=models.CASCADE,
        related_name="authors",
    )
    contact = models.ForeignKey(
        to=Contact,
        on_delete=models.CASCADE,
        related_name="authors",
        blank=True,
        null=True,
    )
    institutions = models.ManyToManyField(
        Institution, related_name="bibliography_authors", blank=True
    )
