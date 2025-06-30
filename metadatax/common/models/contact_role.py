from django.db import models

from .contact import Contact


class ContactRole(models.Model):
    class Type(models.TextChoices):
        MAIN_CONTACT = ("MC", "Main Contact")
        FUNDER = ("F", "Funder")
        PROJECT_OWNER = ("PO", "Project Owner")
        PROJECT_MANAGER = ("PM", "Project Manager")
        DATASET_SUPPLIER = ("DS", "Dataset Supplier")
        DATASET_PRODUCER = ("DP", "Dataset Producer")
        PRODUCTION_DATABASE = ("PD", "Production Database")
        CONTACT_POINT = ("CP", "Contact Point")

    class Meta:
        db_table = "metadatax_common_contactrole"
        unique_together = (("contact", "role"),)

    def __str__(self):
        return f"{ContactRole.Type(self.role).label}: {self.contact}"

    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    role = models.CharField(max_length=2, choices=Type.choices)
