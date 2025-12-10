from django.db import models

from .bibliography import Bibliography
from .__enums__ import BibliographyType


class ConferenceManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(type=BibliographyType.CONFERENCE)


class Conference(Bibliography):
    objects = ConferenceManager()

    class Meta:
        proxy = True
        # constraints = [
        #     CheckConstraint(
        #         name="Conference has required information",
        #         check=Q(
        #             conference_name__isnull=False,
        #             conference_location__isnull=False,
        #         )
        #     ),
        # ]

    def __str__(self):
        return f"{super().__str__()}, {self.conference_name}, {self.conference_location}"
