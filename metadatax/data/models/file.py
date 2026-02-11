"""Acquisition models for metadata app"""
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from metadatax.common.models import Accessibility
from .file_format import FileFormat


class File(models.Model):
    """File"""

    class Meta:
        db_table = "mx_data_file"
        ordering = ("filename",)

    def __str__(self):
        return self.filename

    filename = models.CharField(
        max_length=255, help_text="Name of the file, with extension."
    )
    format = models.ForeignKey(
        to=FileFormat,
        on_delete=models.PROTECT,
        help_text="Format of the audio file.",
        related_name="files",
    )

    storage_location = models.TextField(
        blank=True, null=True, help_text="Description of the path to access the data."
    )
    file_size = models.BigIntegerField(
        null=True,
        blank=True,
        help_text="Total number of bytes of the audio file (in bytes).",
    )
    accessibility = models.TextField(
        choices=Accessibility.choices,
        blank=True,
        null=True,
        default=Accessibility.REQUEST,
        help_text="Accessibility level of the data."
                  " If the availability is not sure or non-uniform within the audio file, "
                  "the default value is upon request.",
    )

    property_type = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT,
        limit_choices_to={
            "model__in": [
                "data.AudioProperties",
                "data.DetectionProperties",
            ]
        },
    )
    property_id = models.PositiveBigIntegerField()
    property = GenericForeignKey("property_type", "property_id")
