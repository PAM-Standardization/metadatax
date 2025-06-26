from django.db import models

from metadatax_common.models import Accessibility, ContactRole
from .financing import Financing
from .project_type import ProjectType


class Project(models.Model):
    """Data acquisition project"""

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    name = models.CharField(
        max_length=255, unique=True, help_text="Name of the project"
    )
    contacts = models.ManyToManyField(
        ContactRole, help_text="Should have at least one 'Main Contact'"
    )  # TODO: constraint

    accessibility = models.CharField(
        choices=Accessibility.choices,
        max_length=1,
        blank=True,
        null=True,
        help_text="Accessibility level of the data. If the availability is not sure or non-uniform within the project, "
        "the default value is upon request.",
    )
    doi = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Digital Object Identifier of the data, if existing.",
    )
    project_type = models.ForeignKey(
        to=ProjectType,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="projects",
        help_text="Description of the type of the project "
        "(e.g., research, marine renewable energies, long monitoring,...).",
    )
    start_date = models.DateField(
        blank=True,
        null=True,
    )
    end_date = models.DateField(
        blank=True,
        null=True,
    )
    project_goal = models.TextField(
        blank=True, null=True, help_text="Description of the goal of the project."
    )
    financing = models.CharField(
        choices=Financing.choices,
        max_length=2,
        blank=True,
        null=True,
    )
