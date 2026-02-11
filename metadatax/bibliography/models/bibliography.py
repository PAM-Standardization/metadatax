from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import QuerySet, Q

from metadatax.utils import custom_fields
from metadatax.common.models import Tag
from .__enums__ import BibliographyStatus, BibliographyType


class Bibliography(models.Model):
    """Bibliography model"""

    class Meta:
        db_table = 'mx_bibliography_bibliography'
        verbose_name_plural = "Bibliography"
        constraints = [
            models.CheckConstraint(
                name="Published bibliography has a publication date",
                check=(Q(status="P", publication_date__isnull=False) | ~Q(status="P")),
            ),
        ]

    def __str__(self):
        return self.title

    title = models.CharField(max_length=255)
    doi = models.CharField(max_length=255, null=True, blank=True, unique=True)

    status = models.CharField(
        choices=BibliographyStatus.choices,
        max_length=1,
    )
    publication_date = custom_fields.DateField(
        null=True, blank=True, help_text="Required for any published bibliography"
    )

    type = models.CharField(
        choices=BibliographyType.choices,
        max_length=1,
    )

    # Article
    journal = models.CharField(max_length=255, null=True, blank=True)
    volumes = models.CharField(max_length=255, null=True, blank=True)
    pages_from = models.PositiveIntegerField(null=True, blank=True)
    pages_to = models.PositiveIntegerField(null=True, blank=True)
    issue_nb = models.PositiveIntegerField(null=True, blank=True)
    article_nb = models.PositiveIntegerField(null=True, blank=True)

    # Conference
    conference_name = models.CharField(max_length=255, null=True, blank=True)
    conference_location = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="format: {City}, {Country}",
    )
    conference_abstract_book_url = models.URLField(null=True, blank=True)

    # Poster
    poster_url = models.URLField(null=True, blank=True)

    # Software
    publication_place = models.CharField(max_length=255, null=True, blank=True)
    repository_url = models.URLField(null=True, blank=True)

    @property
    def publication(self):
        """Get publication status and date when apply"""
        status = BibliographyStatus(self.status).label
        if self.status == BibliographyStatus.PUBLISHED:
            return f"{status} {self.publication_date}"
        return status

    @property
    def tags(self) -> QuerySet[Tag]:
        """Get related tags"""
        return Tag.objects.filter(
            tagged_items__item_type=ContentType.objects.get_for_model(Bibliography),
            tagged_items__item_id=self.pk,
        )
