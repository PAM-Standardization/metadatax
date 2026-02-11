from django.db import models

from .institution import Institution


class Team(models.Model):
    class Meta:
        db_table = "mx_common_team"
        unique_together = ("name", "institution")
        ordering = ("institution",)

    def __str__(self):
        if self.institution is None:
            return self.name
        return f"{self.name} [{self.institution}]"

    name = models.CharField(max_length=255)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    mail = models.EmailField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
