from django.db import models

from .__enums__ import BibliographyType
from .bibliography import Bibliography


class ArticleManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(type=BibliographyType.ARTICLE)


class Article(Bibliography):
    objects = ArticleManager()

    class Meta:
        proxy = True
        # constraints = [
        #     CheckConstraint(
        #         name="Article has required information",
        #         check=Q(journal__isnull=False)
        #     ),
        # ]

    def __str__(self):
        info = []
        if self.journal:
            info.append(str(self.journal))
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
        return f"{super().__str__()}, {", ".join(info)}"
