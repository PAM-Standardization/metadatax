from django.db import models

from .project import Project


class Site(models.Model):
    """Name of the site where the deployment was done"""

    class Meta:
        unique_together = ["name", "project"]
        ordering = ["project", "name"]

    def __str__(self):
        return f"{self.project.name} {self.name}"

    name = models.CharField(
        max_length=255,
        help_text="Name of the platform conceptual location. "
                  "A site may group together several platforms in relatively close proximity, "
                  "or describes a location where regular deployments are carried out.",
    )
    """Name of the generic location"""
    project = models.ForeignKey(
        to=Project,
        related_name="sites",
        on_delete=models.CASCADE,
        help_text="Project associated to this site",
    )
