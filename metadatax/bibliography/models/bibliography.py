from django.db import models
from django.db.models import Q

from .bibliography_article import BibliographyArticle
from .bibliography_conference import BibliographyConference
from .bibliography_poster import BibliographyPoster
from .bibliography_software import BibliographySoftware
from .tag import Tag


class Bibliography(models.Model):
    """Bibliography model"""

    class Status(models.TextChoices):
        """Bibliography publication status"""

        UPCOMING = ("U", "Upcoming")
        PUBLISHED = ("P", "Published")

    class Type(models.TextChoices):
        """Type of bibliography"""

        SOFTWARE = ("S", "Software")
        ARTICLE = ("A", "Article")
        CONFERENCE = ("C", "Conference")
        POSTER = ("P", "Poster")

    class Meta:
        verbose_name_plural = "Bibliography"
        constraints = [
            models.CheckConstraint(
                name="Published bibliography has a publication date",
                check=(Q(status="P", publication_date__isnull=False) | ~Q(status="P")),
            ),
            models.CheckConstraint(
                name="Article has required information",
                check=(~Q(type="A") & Q(article_information__isnull=True))
                | Q(type="A", article_information__isnull=False),
            ),
            models.CheckConstraint(
                name="Software has required information",
                check=(~Q(type="S") & Q(software_information__isnull=True))
                | Q(type="S", software_information__isnull=False),
            ),
            models.CheckConstraint(
                name="Conference has required information",
                check=(
                    ~Q(type="C") & ~Q(type="P") & Q(conference_information__isnull=True)
                )
                | Q(type="C", conference_information__isnull=False),
            ),
            models.CheckConstraint(
                name="Poster has required information",
                check=(~Q(type="P") & Q(poster_information__isnull=True))
                | Q(type="P", poster_information__isnull=False),
            ),
        ]

    def __str__(self):
        return self.title

    title = models.CharField(max_length=255)
    doi = models.CharField(max_length=255, null=True, blank=True, unique=True)
    tags = models.ManyToManyField(Tag, blank=True)

    status = models.CharField(
        choices=Status.choices,
        max_length=1,
    )
    publication_date = models.DateField(
        null=True, blank=True, help_text="Required for any published bibliography"
    )

    type = models.CharField(
        choices=Type.choices,
        max_length=1,
    )

    software_information = models.OneToOneField(
        BibliographySoftware,
        related_name="bibliography",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    article_information = models.OneToOneField(
        BibliographyArticle,
        related_name="bibliography",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    conference_information = models.ForeignKey(
        BibliographyConference,
        related_name="bibliography",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    poster_information = models.OneToOneField(
        BibliographyPoster,
        related_name="bibliography",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    @property
    def publication(self):
        """Get publication status and date when apply"""
        status = Bibliography.Status(self.status).label
        if self.status == Bibliography.Status.PUBLISHED:
            return f"{status} {self.publication_date}"
        return status
