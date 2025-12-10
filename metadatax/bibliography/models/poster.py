from django.db import models

from .conference import Conference
from .__enums__ import BibliographyType


class PosterManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(type=BibliographyType.POSTER)


class Poster(Conference):
    objects = PosterManager()

    class Meta:
        proxy = True
        # constraints = [
        #     CheckConstraint(
        #         name="Poster has required information",
        #         check=Q(
        #             conference_name__isnull=False,
        #             conference_location__isnull=False,
        #         )
        #     ),
        # ]

    def __str__(self):
        if self.poster_url:
            return f"{super().__str__()}, {self.poster_url}"
        return super().__str__()
