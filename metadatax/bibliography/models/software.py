from django.db import models

from .bibliography import Bibliography
from .__enums__ import BibliographyType


class SoftwareManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(type=BibliographyType.SOFTWARE)


class Software(Bibliography):
    objects = SoftwareManager()

    class Meta:
        proxy = True
        # constraints = [
        #     CheckConstraint(
        #         name="Software has required information",
        #         check=Q(
        #             publication_place__isnull=False,
        #         )
        #     ),
        # ]

    def __str__(self):
        info = []
        if self.publication_place:
            info.append(self.publication_place)
        if self.repository_url:
            info.append(self.repository_url)
        return f"{super().__str__()}, {", ".join(info)}"
