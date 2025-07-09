from django.db import models


class BibliographyArticle(models.Model):
    journal = models.CharField(max_length=255, help_text="Required for an article")
    volumes = models.CharField(max_length=255, null=True, blank=True)
    pages_from = models.PositiveIntegerField(null=True, blank=True)
    pages_to = models.PositiveIntegerField(null=True, blank=True)
    issue_nb = models.PositiveIntegerField(null=True, blank=True)
    article_nb = models.PositiveIntegerField(null=True, blank=True)
