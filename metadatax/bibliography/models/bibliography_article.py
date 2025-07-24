from django.db import models


class BibliographyArticle(models.Model):
    def __str__(self):
        info = [self.journal]
        if self.volumes:
            info.append(str(self.volumes))
        if self.pages_from:
            if self.pages_to:
                info.append(f"{self.pages_from}-{self.pages_to}")
            else:
                info.append(str(self.pages_from))
        if self.issue_nb:
            info.append(str(self.issue_nb))
        if self.article_nb:
            info.append(str(self.article_nb))
        return ", ".join(info)

    journal = models.CharField(max_length=255, help_text="Required for an article")
    volumes = models.CharField(max_length=255, null=True, blank=True)
    pages_from = models.PositiveIntegerField(null=True, blank=True)
    pages_to = models.PositiveIntegerField(null=True, blank=True)
    issue_nb = models.PositiveIntegerField(null=True, blank=True)
    article_nb = models.PositiveIntegerField(null=True, blank=True)
