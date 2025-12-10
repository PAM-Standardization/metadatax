from django.contrib.contenttypes.models import ContentType
from django.db import models

from .properties import AudioProperties
from .file import File


class AudioFileManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(property_type=ContentType.objects.get_for_model(AudioProperties))


class AudioFile(File):
    objects = AudioFileManager()

    class Meta:
        proxy = True

    @property
    def audio_properties(self) -> AudioProperties:
        return self.property

    def delete(self, using=None, keep_parents=False):
        p = self.audio_properties
        info = super().delete(using, keep_parents)
        p.delete()
        return info
