from django.db import models

from .properties import DetectionProperties
from .file import File


class DetectionFileManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(property_type__model="DetectionProperties".lower())


class DetectionFile(File):
    objects = DetectionFileManager()

    class Meta:
        proxy = True

    @property
    def detection_properties(self) -> DetectionProperties:
        return self.property

    def delete(self, using=None, keep_parents=False):
        p = self.detection_properties
        info = super().delete(using, keep_parents)
        p.delete()
        return info
