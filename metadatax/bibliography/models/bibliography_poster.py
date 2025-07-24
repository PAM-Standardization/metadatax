from django.db import models


class BibliographyPoster(models.Model):
    def __str__(self):
        return self.poster_url or super().__str__()

    poster_url = models.URLField(null=True, blank=True)
