from django.db import models
from django.db.models import Q

from .contact import Contact
from .institution import Institution


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
        constraints = [
            models.CheckConstraint(
                name="has_contact_or_institution",
                check=Q(contact__isnull=False) | Q(institution__isnull=False),
            )
        ]
        ordering = ("role", "contact", "institution")

    def __str__(self):
        if self.contact:
            return f"{ContactRole.Type(self.role).label}: {self.contact}"
        return f"{ContactRole.Type(self.role).label}: {self.institution}"

    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE, related_name="roles", blank=True, null=True
    )
    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE,
        related_name="roles",
        blank=True,
        null=True,
    )
    role = models.CharField(max_length=2, choices=Type.choices)
