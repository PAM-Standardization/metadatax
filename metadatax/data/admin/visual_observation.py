from django.contrib import admin
from django_extension.admin import ExtendedModelAdmin

from metadatax.data.models import VisualObservation
from metadatax.utils import admin_display_min_max


@admin.register(VisualObservation)
class VisualObservationAdmin(ExtendedModelAdmin):
    list_display = [
        "id",
        "deployment",
        "source",
        "start_datetime",
        "end_datetime",
        "count",
        "start_distance",
        "end_distance",
        "additional_information",
        "young_presence",
        "other_human_activity_presence",
        "display_behaviors",
        "display_reactions_to_boat",
    ]
    search_fields = [
        "deployment__platform__name",
        "deployment__site__name",
        "deployment__campaign__name",
        "deployment__name",
        "source__taxon",
        "source__code_name",
        "source__latin_name",
        "source__french_name",
        "source__english_name",
    ]
    list_filter = [
        "young_presence",
        "other_human_activity_presence",
        "behaviors",
        "reactions_to_boat",
    ]

    @admin.display(description="Count")
    def count(self, obj: VisualObservation):
        return admin_display_min_max(obj, 'count_min', 'count_max')

    @admin.display(description="Start distance")
    def start_distance(self, obj: VisualObservation):
        return admin_display_min_max(obj, 'start_distance_min', 'start_distance_max')

    @admin.display(description="End distance")
    def end_distance(self, obj: VisualObservation):
        return admin_display_min_max(obj, 'end_distance_min', 'end_distance_max')

    @admin.display(description="Behaviors")
    def display_behaviors(self, obj: VisualObservation):
        return self.list_queryset(queryset=obj.behaviors.all())

    @admin.display(description="Boat reactions")
    def display_reactions_to_boat(self, obj: VisualObservation):
        return self.list_queryset(queryset=obj.reactions_to_boat.all())
