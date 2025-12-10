"""Acquisition models for metadata app"""
from django.db import models
from metadatax.common.models import Accessibility

from .audio_properties import AudioProperties
from .detection_properties import DetectionProperties
from .file_format import FileFormat


class File(models.Model):
    """File"""

    class Meta:
        db_table = "metadatax_data_file"
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

    audio_properties = models.OneToOneField(
        AudioProperties,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="file",
        help_text="Each property is dedicated to one file.",
    )
    detection_properties = models.OneToOneField(
        DetectionProperties,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="file",
        help_text="Each property is dedicated to one file.",
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
