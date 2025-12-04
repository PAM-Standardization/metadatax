from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from metadatax.common.models.enums import Role


class ContactRelation(models.Model):

    class Meta:
        db_table = "mx_common_contactrelation"
        ordering = ("role",)

    def __str__(self):
        return f"{Role(self.role).label}: {self.contact}"

    role = models.CharField(max_length=2, choices=Role.choices)

    contact_type = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT,
        limit_choices_to={
            "model__in": [
                "common.Person",
                "common.Team",
                "common.Institution",
            ]
        },
    )
    contact_id = models.PositiveBigIntegerField()
    contact = GenericForeignKey("contact_type", "contact_id")

