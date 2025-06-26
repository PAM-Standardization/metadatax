from django.db import models

from .project import Project


class Campaign(models.Model):
    """Name of the campaign during which the deployment was done"""

    class Meta:
        unique_together = ["name", "project"]
        ordering = ["project", "name"]

    def __str__(self):
        return f"{self.project.name} {self.name}"

    name = models.CharField(
        max_length=255,
        help_text="Name of the campaign during which the instrument was deployed.",
    )
    project = models.ForeignKey(
        to=Project,
        related_name="campaigns",
        on_delete=models.CASCADE,
        help_text="Project associated to this campaign",
    )
