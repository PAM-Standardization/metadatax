from django.db import models

from metadatax.acquisition.models.deployment import Deployment
from metadatax.ontology.models import Source, Behavior
from metadatax.utils import custom_fields


class VisualObservation(models.Model):
    """VisualObservation"""

    class Meta:
        db_table = "mx_data_visualobservation"

    def __str__(self):
        return f"{self.source} [{self.start_datetime}]"

    deployment = models.ForeignKey(
        to=Deployment,
        on_delete=models.PROTECT,
        related_name="visual_observations",
    )
    source = models.ForeignKey(
        to=Source,
        on_delete=models.PROTECT,
        related_name="visual_observations",
    )
    start_datetime = custom_fields.DateTimeField(
        help_text="Start datetime for the observation."
    )
    end_datetime = custom_fields.DateTimeField(
        help_text="End datetime for the observation."
    )

    count_min = models.IntegerField(
        blank=True, null=True, help_text="Minimal number of source observed."
    )
    count_max = models.IntegerField(
        blank=True, null=True, help_text="Maximal number of source observed."
    )
    start_distance_min = models.IntegerField(
        blank=True, null=True, help_text="Minimal distance at the start of the observation."
    )
    start_distance_max = models.IntegerField(
        blank=True, null=True, help_text="Maximal distance at the start of the observation."
    )
    end_distance_min = models.IntegerField(
        blank=True, null=True, help_text="Minimal distance at the end of the observation."
    )
    end_distance_max = models.IntegerField(
        blank=True, null=True, help_text="Maximal distance at the end of the observation."
    )
    young_presence = models.BooleanField(
        blank=True, null=True, help_text="Young animals presence during the observation."
    )
    other_human_activity_presence = models.BooleanField(
        blank=True, null=True,
        help_text="Human activity presence during the observation (excluding the observation process)."
    )
    behaviors = models.ManyToManyField(
        to=Behavior,
        related_name="visual_observations",
        blank=True,
    )
    reactions_to_boat = models.ManyToManyField(
        to=Behavior,
        related_name="visual_observation_reactions",
        blank=True,
    )

    additional_information = models.TextField(
        blank=True,
        null=True,
        help_text="Optional information over the observation.",
    )
