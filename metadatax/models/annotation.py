"""Annotation models for metadata app"""
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver


from meta_auth.models import User


class AnnotationType(models.TextChoices):
    WEAK = ("W", "Weak")
    BOX = ("B", "Box")
    PICKING = ("P", "Picking")
    CONTOURING = ("C", "Contouring")


class AnnotationLevel(models.TextChoices):
    BEGINNER = ("B", "Beginner")
    EXPERT = ("E", "Expert")


class Confidence(models.Model):
    label = models.TextField()
    is_trusted = models.BooleanField()


class Label(models.Model):
    source = models.TextField()
    type = models.TextField()


class Annotation(models.Model):
    class Meta:
        verbose_name = "Annotation"

    def __str__(self):
        return self.name

    absolute_start = models.DateTimeField(
        verbose_name="Absolute start (UTC)",
    )
    absolute_end = models.DateTimeField(
        verbose_name="Absolute end (UTC)",
    )

    min_frequency = models.FloatField()
    max_frequency = models.FloatField()

    type = models.TextField(choices=AnnotationType.choices, default=AnnotationType.BOX)

    confidence = models.ForeignKey(
        to=Confidence, on_delete=models.SET_NULL(), blank=True, null=True
    )
    label = models.ForeignKey(
        to=Label,
        on_delete=models.PROTECT(),
    )

    origin
