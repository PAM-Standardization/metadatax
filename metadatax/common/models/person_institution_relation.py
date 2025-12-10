from django.db import models


class PersonInstitutionRelation(models.Model):

    class Meta:
        db_table = "mx_common_personinstitutionrelation"
        unique_together = ("person", "institution", "team")

    def __str__(self):
        name = f"{self.person} - {self.institution}"
        if self.team:
            return f"{name} ({self.team.name})"
        return name

    person = models.ForeignKey("common.Person", related_name="institution_relations", on_delete=models.CASCADE)
    institution = models.ForeignKey("common.Institution", related_name="contact_relations", on_delete=models.CASCADE)

    team = models.ForeignKey("common.Team", related_name="contact_relations", on_delete=models.CASCADE, blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
