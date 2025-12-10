from django.db import models

from .institution import Institution
from .person_institution_relation import PersonInstitutionRelation
from .team import Team


class Person(models.Model):
    """Person model"""

    class Meta:
        db_table = "mx_common_person"
        unique_together = ("first_name", "last_name")
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    mail = models.EmailField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)

    institutions = models.ManyToManyField(Institution, related_name="persons", through=PersonInstitutionRelation)
    teams = models.ManyToManyField(Team, related_name="persons", through=PersonInstitutionRelation)

    @property
    def initial_names(self):
        names = self.first_name.split("-")
        initial_first_name = "-".join([f"{n[0]}." for n in names])
        return f"{self.last_name}, {initial_first_name}"
