from django.db import models


class ProjectType(models.Model):
    """Indicates the type of the project. (research, marine renewable energies, long monitoring).
    Can contain multiple values"""

    class Meta:
        ordering = ["name"]
        db_table = "metadatax_acquisition_projecttype"

    def __str__(self):
        return self.name

    name = models.CharField(
        max_length=255, unique=True, help_text="Description of the type of the project"
    )
