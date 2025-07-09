from django.db import models


class BibliographySoftware(models.Model):

    publication_place = models.CharField(
        max_length=255, help_text="Required for a software"
    )
    repository_url = models.URLField(null=True, blank=True)
