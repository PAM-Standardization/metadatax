from django.db import models


class BibliographyPoster(models.Model):
    poster_url = models.URLField(null=True, blank=True)
