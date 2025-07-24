from django.db import models


class BibliographySoftware(models.Model):
    def __str__(self):
        info = [self.publication_place]
        if self.repository_url:
            info.append(self.repository_url)
        return ", ".join(info)

    publication_place = models.CharField(
        max_length=255, help_text="Required for a software"
    )
    repository_url = models.URLField(null=True, blank=True)
